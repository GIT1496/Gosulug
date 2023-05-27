from django.contrib import admin
from django.contrib import admin
from .models import Reestr_2, Reestr_1
from SANZ_1.models import SEZ1, SEZItem
from OTKAZ.models import OTKItem
from .models import Reestr1Summary, Reestr2Summary
from django.db.models import Count
from django.db.models import Sum
from datetime import datetime
from rangefilter.filters import DateRangeFilterBuilder, DateTimeRangeFilterBuilder, NumericRangeFilterBuilder

from django.db.models import DateTimeField
from django.db.models import Min
from django.db.models import Max
from django.db.models.functions import Trunc


@admin.register(Reestr1Summary)
class Reestr1SummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/reestr1_summary_change_list.html'
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
            'VID': Count('vid'),
            'ID': Count('id'),
            'NAMBER': Count('namber'),
        }

        response.context_data['summary'] = list(
            qs
            .values('vid','namber','id')
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
            "date_rendering",
            DateTimeRangeFilterBuilder(
                title="Дата оказания услуги",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_rendering", NumericRangeFilterBuilder()),
    'sp')

    def get_next_in_date_hierarchy(request, date_hierarchy):
            if date_hierarchy + '__day' in request.GET:
                return 'hour'
            if date_hierarchy + '__month' in request.GET:
                return 'day'
            if date_hierarchy + '__year' in request.GET:
                return 'week'
            return 'month'


@admin.register(Reestr2Summary)
class Reestr2SummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/reestr2_summary_change_list.html'
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
            'APP': Count('Applicant'),
            'ID': Count('id'),
            'NAMBER': Count('namber'),
        }

        response.context_data['summary'] = list(
            qs
            .values('Applicant','namber','id')
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
            "date_rendering",
            DateTimeRangeFilterBuilder(
                title="Дата оказания услуги",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_rendering", NumericRangeFilterBuilder()),
    'cl')

    def get_next_in_date_hierarchy(request, date_hierarchy):
            if date_hierarchy + '__day' in request.GET:
                return 'hour'
            if date_hierarchy + '__month' in request.GET:
                return 'day'
            if date_hierarchy + '__year' in request.GET:
                return 'week'
            return 'month'




class SEZItemInline(admin.TabularInline):
    model = SEZItem
    raw_id_fields = ['SEZ']

class OTKItemInline(admin.TabularInline):
    model = OTKItem
    raw_id_fields = ['otk']

class Reestr_2Admin(admin.ModelAdmin):
    list_display = ('id', 'namber', 'date_creation', 'date_rendering','fact_adr','cl')  # Отображение полей
    list_display_links = ('namber', 'date_creation')  # Установка ссылок на атрибуты
    search_fields = ('namber', 'cl')  # Поиск по полям
    list_filter = ['namber', "date_rendering"]

    inlines = [OTKItemInline]

admin.site.register(Reestr_2, Reestr_2Admin)

class Reestr_1Admin(admin.ModelAdmin):
    list_display = ('id','namber', 'date_creation', 'date_rendering','predpr','vid')  # Отображение полей
    list_display_links = ('namber', 'date_creation')  # Установка ссылок на атрибуты
    search_fields = ('namber', 'vid')  # Поиск по полям
    list_filter = (
        ("date_creation", DateRangeFilterBuilder()),
        (
            "date_rendering",
            DateTimeRangeFilterBuilder(
                title="Дата оказания услуги",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_rendering", NumericRangeFilterBuilder()),
    )
    inlines = [SEZItemInline, OTKItemInline]





admin.site.register(Reestr_1, Reestr_1Admin)

# Register your models here.
# Register your models here.
