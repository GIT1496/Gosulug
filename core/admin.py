from django.contrib import admin
from .models import Reestr_2, Reestr_1
from SANZ_1.models import SEZItem
from OTKAZ.models import OTKItem

# Модули для анализа данных
from .models import Reestr1Summary, Reestr2Summary
from django.db.models import Count

# Модули для расширеной фильтрации по датам в джанго
from datetime import datetime
from rangefilter.filters import DateRangeFilterBuilder, DateTimeRangeFilterBuilder, NumericRangeFilterBuilder
from django.db.models import DateTimeField
from django.db.models import Min
from django.db.models import Max
from django.db.models.functions import Trunc


"""Дашборды в панели администратора"""
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
        def get_next_in_date_creation(request, date_hierarchy):
            if date_hierarchy + '__day' in request.GET:
                return 'hour'
            if date_hierarchy + '__month' in request.GET:
                return 'day'
            if date_hierarchy + '__year' in request.GET:
                return 'week'
            return 'year'

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
    'sp', 'dejat')






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






"""Отображение моделей в панели администратора"""

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
        ("date_creation", NumericRangeFilterBuilder()), "Vip"
    )

    inlines = [OTKItemInline]

admin.site.register(Reestr_2, Reestr_2Admin)

class Reestr_1Admin(admin.ModelAdmin):
    list_display = ('id','namber', 'date_creation', 'date_rendering','predpr','vid','dejat')  # Отображение полей
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
        ("date_rendering", NumericRangeFilterBuilder()),"Vip"
    )
    inlines = [SEZItemInline, OTKItemInline]





admin.site.register(Reestr_1, Reestr_1Admin)

# Register your models here.
# Register your models here.
