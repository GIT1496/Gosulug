from django.contrib import admin
from .models import OTK, OTKItem,OTKAZSummary
from django.db.models import DateTimeField
from django.db.models import Count
from django.db.models.functions import Trunc
from rangefilter.filters import DateRangeFilterBuilder, DateTimeRangeFilterBuilder, NumericRangeFilterBuilder
from datetime import datetime

"""Дашборды в панели администратора"""
@admin.register(OTKAZSummary)
class OTKAZSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/otkaz_summary_change_list.html'
    date_hierarchy = 'date_creation'

    def changelist_view(self, request, extra_context=None):

        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'PRICH': Count('prich'),
            'ID': Count('id'),
            'NAMBER': Count('Nomer1'),
        }

        response.context_data['summary'] = list(
            qs
            .values('prich','Nomer1','id')
            .annotate(**metrics)
            .order_by('-date_creation')
        )

        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )

        def get_next_in_date_creation(request, date_hierarchy):
            if date_hierarchy + '__day' in request.GET:
                return 'hour'
            if date_hierarchy + '__month' in request.GET:
                return 'day'
            if date_hierarchy + '__year' in request.GET:
                return 'week'
            return 'month'

        period = get_next_in_date_creation(request, self.date_hierarchy)
        response.context_data['period'] = period
        summary_over_time = qs.annotate(
            period=Trunc(
                'date_creation',
                period,
                output_field=DateTimeField(),
            ),
        ).values('period').annotate(total=Count('id')).order_by('period')
        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': x['total']
        } for x in summary_over_time]



        return response

    list_filter =(
        ("date_creation", DateRangeFilterBuilder()),
        (
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата оказания услуги",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),
    'prich')


"""Отображение моделей в панели администратора"""
class OTKItemInline(admin.TabularInline):
    model = OTKItem
    raw_id_fields = ['product1', 'product2']


class OTKAdmin(admin.ModelAdmin):
    list_display = ('Nomer1', 'prich', 'vidano')
    list_display_links = ('Nomer1', 'prich', 'vidano')
    list_filter = ['Nomer1', "date_creation"]
    inlines = [OTKItemInline]


admin.site.register(OTK,OTKAdmin)
# # Register your models here.
# # Register your models here.
# # Register your models here.
