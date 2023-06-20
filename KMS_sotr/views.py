from django.shortcuts import render
from django.views.generic import ListView
from .models import NPA_SEZ,NPA_UVED,NPA_SZZ,NPA_GOSREG,NPA_LICENZ,OPT_STAND, ADM_REG
from .util import Default_value

"""Классы для отображения моделей приложения на стороне пользователей"""
class NSEZListView(ListView, Default_value):  # Возврат листа объектов
    model = NPA_SEZ # определение таблицы для взаимодействия
    form_class = NPA_SEZ
    template_name = 'NPA/NSEZ-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'NPA_SEZ'  # Отправка данных по заданному ключу (object_list)
    extra_context = {'title': 'Реестр НПА по СЭЗ'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = NPA_SEZ.objects.order_by('title')
        context = super(NSEZListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5

class NPA_UVEDListView(ListView, Default_value):  # Возврат листа объектов
    model = NPA_UVED # определение таблицы для взаимодействия
    form_class = NPA_UVED
    template_name = 'NPA/NUVED-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'NPA_UVED'  # Отправка данных по заданному ключу (object_list)
    extra_context = {'title': 'Реестр НПА по уведомлениям'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = NPA_SEZ.objects.order_by('title')
        context = super(NPA_UVEDListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5


class NPA_SZZListView(ListView, Default_value):  # Возврат листа объектов
    model = NPA_SZZ  # определение таблицы для взаимодействия
    form_class = NPA_SZZ
    template_name = 'NPA/NPA_SZZ-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'NPA_SZZ'  # Отправка данных по заданному ключу (object_list)
    extra_context = {'title': 'Реестр НПА по санитарно-защитным зонам'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = NPA_SEZ.objects.order_by('title')
        context = super(NPA_SZZListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5

class NPA_GOSREGListView(ListView, Default_value):  # Возврат листа объектов
    model = NPA_GOSREG  # определение таблицы для взаимодействия
    form_class = NPA_GOSREG
    template_name = 'NPA/NPA_GOSREG-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'NPA_GOSREG'  # Отправка данных по заданному ключу (object_list)
    extra_context = {'title': 'Реестр НПА по свидетельствам о государственной регистрации продукции'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = NPA_GOSREG.objects.order_by('title')
        context = super(NPA_GOSREGListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5


class NPA_LICENZListView(ListView, Default_value):  # Возврат листа объектов
    model = NPA_LICENZ  # определение таблицы для взаимодействия
    form_class = NPA_LICENZ
    template_name = 'NPA/NPA_LICENZ-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'NPA_LICENZ'  # Отправка данных по заданному ключу (object_list)
    extra_context = {'title': 'Реестр НПА по уведомелниям о начале осуществления предпринимательской деятельности'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = NPA_LICENZ.objects.order_by('title')
        context = super(NPA_LICENZListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5


class OPT_STANDListView(ListView, Default_value):  # Возврат листа объектов
    model = OPT_STAND  # определение таблицы для взаимодействия
    form_class = OPT_STAND
    template_name = 'OPTS/OPT_STAND-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'OPT_STAND'  # Отправка данных по заданному ключу (object_list)
    extra_context = {'title': 'Оптимизированные стандарты оказания государственных услуг'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = OPT_STAND.objects.order_by('title')
        context = super(OPT_STANDListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5

class ADM_REGListView(ListView, Default_value):  # Возврат листа объектов
    model = ADM_REG  # определение таблицы для взаимодействия
    form_class = ADM_REG
    template_name = 'NPA/ADM_REG-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'ADM_REG'  # Отправка данных по заданному ключу (object_list)
    extra_context = {'title': 'Административные регламенты предоставления государственных услуг'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = OPT_STAND.objects.order_by('title')
        context = super(ADM_REGListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5