from django.contrib import admin
from django.contrib import admin
from .models import SEZ1, SEZItem, SEZSummary,LICSummary, SVIDSummary, LIC1, RESH1, RESHItem, SVID, Pereoformlen

from django.db.models import DateTimeField
from django.db.models import Min
from django.db.models import Max
from django.db.models import Count
from django.db.models.functions import Trunc
from rangefilter.filters import DateRangeFilterBuilder, DateTimeRangeFilterBuilder, NumericRangeFilterBuilder
from datetime import datetime

"""Дашборды в панели администратора"""
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
            'ID': Count('date_creation'),
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
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата оказания услуги",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),'deistv',
    )


@admin.register(LICSummary)
class LICSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/LIC_summary_change_list.html'
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
            'NAMBER': Count('Nomer'),
            'LIC': Count('vid'),
            'VID': Count('id'),
        }

        response.context_data['summary'] = list(
            qs
            .values('Nomer','vid','id')
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
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата оказания услуги",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),'vid',
    )



@admin.register(SVIDSummary)
class SVIDSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/SVID_summary_change_list.html'
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
            'NAMBER': Count('Nomer'),
            'F': Count('firm'),
            'O': Count('obl'),
        }

        response.context_data['summary'] = list(
            qs
            .values('Nomer','firm','obl')
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
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата оказания услуги",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),'obl',
    )



"""Отображение моделей в панели администратора"""
class SEZItemInline(admin.TabularInline):
    model = SEZItem
    raw_id_fields = ['product']

class RESHItemInline(admin.TabularInline):
    model = RESHItem
    raw_id_fields = ['resh']




class SEZAdmin(admin.ModelAdmin):
    list_display = ('id','Nomer', 'tipogr', 'vidano')
    list_display_links = ('Nomer', 'tipogr', 'vidano')
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
        ("date_creation", NumericRangeFilterBuilder()), "deistv")
    inlines = [SEZItemInline]

admin.site.register(SEZ1, SEZAdmin)
class LICAdmin(admin.ModelAdmin):
    list_display = ('date_creation', 'Nomer',)
    list_display_links = ("date_creation", 'Nomer')
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
        ("date_creation", NumericRangeFilterBuilder()),
    )

admin.site.register(LIC1,LICAdmin)
class SVIDAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nomer', "firm")
    list_display_links = ('Nomer', "firm")
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
        ("date_creation", NumericRangeFilterBuilder()),
    )
admin.site.register(SVID,SVIDAdmin)

class PEREdmin(admin.ModelAdmin):
    list_display = ('id', 'nomer', "nomer2")
    list_display_links = ('nomer', "nomer2")
    list_filter = (
        ("date", DateRangeFilterBuilder()),
        (
            "date",
            DateTimeRangeFilterBuilder(
                title="Дата оказания услуги",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date", NumericRangeFilterBuilder()),
    )


admin.site.register(Pereoformlen,PEREdmin)
class RESHAdmin(admin.ModelAdmin):
    list_display = ('namber', "date_creation")
    list_display_links = ('namber', "date_creation")
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
        ("date_creation", NumericRangeFilterBuilder()),
    )

admin.site.register(RESH1,RESHAdmin)


