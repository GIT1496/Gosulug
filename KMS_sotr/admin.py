from django.contrib import admin
from .models import NPA_SEZ,NPA_UVED,NPA_SZZ,NPA_GOSREG,NPA_LICENZ,OPT_STAND, ADM_REG
from datetime import datetime
from rangefilter.filters import DateRangeFilterBuilder, DateTimeRangeFilterBuilder, NumericRangeFilterBuilder



class NPA_SEZAdmin(admin.ModelAdmin):
    list_display = ('title', 'kr_op')  # Отображение полей
    list_display_links = ('title', 'kr_op')  # Установка ссылок на атрибуты
    search_fields = ('title', 'kr_op')  # Поиск по полям
    list_filter = (
        ("date_creation", DateRangeFilterBuilder()),
        (
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата документа",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),
    )


admin.site.register(NPA_SEZ, NPA_SEZAdmin)

class NPA_UVEDAdmin(admin.ModelAdmin):
    list_display = ('title', 'kr_op')  # Отображение полей
    list_display_links = ('title', 'kr_op')  # Установка ссылок на атрибуты
    search_fields = ('title', 'kr_op')  # Поиск по полям
    list_filter = (
        ("date_creation", DateRangeFilterBuilder()),
        (
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата документа",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),
    )


admin.site.register(NPA_UVED, NPA_UVEDAdmin)


class NPA_SZZAdmin(admin.ModelAdmin):
    list_display = ('title', 'kr_op')  # Отображение полей
    list_display_links = ('title', 'kr_op')  # Установка ссылок на атрибуты
    search_fields = ('title', 'kr_op')  # Поиск по полям
    list_filter = (
        ("date_creation", DateRangeFilterBuilder()),
        (
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата документа",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),
    )


admin.site.register(NPA_SZZ, NPA_SZZAdmin)

class NPA_GOSREGAdmin(admin.ModelAdmin):
    list_display = ('title', 'kr_op')  # Отображение полей
    list_display_links = ('title', 'kr_op')  # Установка ссылок на атрибуты
    search_fields = ('title', 'kr_op')  # Поиск по полям
    list_filter = (
        ("date_creation", DateRangeFilterBuilder()),
        (
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата документа",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),
    )


admin.site.register(NPA_GOSREG, NPA_GOSREGAdmin)

class NPA_LICENZAdmin(admin.ModelAdmin):
    list_display = ('title', 'kr_op')  # Отображение полей
    list_display_links = ('title', 'kr_op')  # Установка ссылок на атрибуты
    search_fields = ('title', 'kr_op')  # Поиск по полям
    list_filter = (
        ("date_creation", DateRangeFilterBuilder()),
        (
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата документа",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),
    )


admin.site.register(NPA_LICENZ, NPA_LICENZAdmin)

class OPT_STANDAdmin(admin.ModelAdmin):
    list_display = ('title', 'kr_op')  # Отображение полей
    list_display_links = ('title', 'kr_op')  # Установка ссылок на атрибуты
    search_fields = ('title', 'kr_op')  # Поиск по полям
    list_filter = (
        ("date_creation", DateRangeFilterBuilder()),
        (
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата документа",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),
    )


admin.site.register(OPT_STAND, OPT_STANDAdmin)

class ADM_REGAdmin(admin.ModelAdmin):
    list_display = ('title', 'kr_op')  # Отображение полей
    list_display_links = ('title', 'kr_op')  # Установка ссылок на атрибуты
    search_fields = ('title', 'kr_op')  # Поиск по полям
    list_filter = (
        ("date_creation", DateRangeFilterBuilder()),
        (
            "date_creation",
            DateTimeRangeFilterBuilder(
                title="Дата документа",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("date_creation", NumericRangeFilterBuilder()),
    )


admin.site.register(ADM_REG, ADM_REGAdmin)

