from django.contrib import admin
from django.contrib import admin
from .models import SEZ1, SEZItem, SEZSummary,LIC1, RESH1, RESHItem
from django.db.models import DateTimeField
from django.db.models import Min
from django.db.models import Max
from django.db.models import Count
from django.db.models.functions import Trunc
from rangefilter.filters import DateRangeFilterBuilder, DateTimeRangeFilterBuilder, NumericRangeFilterBuilder
from datetime import datetime

@admin.register(SEZSummary)
class SEZSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/SEZ_summary_change_list.html'
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
            'TIP': Count('tipogr'),
            'ID': Count('id'),
            'NAMBER': Count('Nomer'),
        }

        response.context_data['summary'] = list(
            qs
            .values('tipogr','Nomer','id')
            .annotate(**metrics)
            .order_by('-date_creation')
        )

        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )


        summary_over_time = qs.annotate(
            period=Trunc(
                'date_creation',
                'day',
                output_field=DateTimeField(),
            ),


        ).values('period').annotate(total=Count('id')).order_by('period')
        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)
        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': x['total']
        } for x in summary_over_time]




        return response

    list_filter = (
        ("date_creation", DateRangeFilterBuilder()),
        (
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата оказания услуги",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),'deistv',
    )



class SEZItemInline(admin.TabularInline):
    model = SEZItem
    raw_id_fields = ['product']

class RESHItemInline(admin.TabularInline):
    model = RESHItem
    raw_id_fields = ['resh']


class SEZAdmin(admin.ModelAdmin):
    list_display = ('id','Nomer', 'tipogr', 'vidano')
    list_display_links = ('Nomer', 'tipogr', 'vidano')
    list_filter = ['Nomer', "date_creation"]
    inlines = [SEZItemInline]

admin.site.register(SEZ1, SEZAdmin)
class LICAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nomer', "licenz")

admin.site.register(LIC1,LICAdmin)

class RESHAdmin(admin.ModelAdmin):
    list_display = ('namber', "date_creation")

admin.site.register(RESH1,RESHAdmin)


# Register your models here.
# Register your models here.


# Register your models here.
