from django.shortcuts import render
from .models import OTKItem, Reestr_1, Reestr_2
from .forms import OTKCreateForm

from basket.basket import Basket, Basket_resh
from django.views.generic import TemplateView, ListView
from .util import Default_value


"""Обработка внесения отказов через сессию"""

def add_OTKAZ_SEZ(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OTKCreateForm(request.POST)
        if form.is_valid():
            otk = form.save()
            for item in basket:
                    OTKItem.objects.create(otk=otk,
                                       product1=item['SEZ'],
                                        status1="Отказ в оказании государственной услуги"),
                    Reestr_1.objects.filter(namber=item['SEZ']).update(Vip=True)
            # очистка корзины
            basket.clear()
            # # order_create.delay(SEZ.id)
            return render(request, 'orders1/order1/created1.html',
                          {'otk': otk })
    else:
        form = OTKCreateForm

    return render(request, 'orders1/order1/create_OTKAZ.html',
                  {'basket': basket, 'form': form})

def add_OTKAZ_RESH(request):
    basket = Basket_resh(request)
    if request.method == 'POST':
        form = OTKCreateForm(request.POST)
        if form.is_valid():
            otk = form.save()
            for item in basket:
                    OTKItem.objects.create(otk=otk,
                                           product2=item['RES1'],
                                           status1="Отказ в оказании государственной услуги"),
                    Reestr_2.objects.filter(namber=item['RES1']).update(Vip=True)
            # очистка корзины
            basket.clear()
            # # order_create.delay(SEZ.id)
            return render(request, 'orders1/order1/created1.html',
                          {'otk': otk })
    else:
        form = OTKCreateForm

    return render(request, 'orders1/order1/create_OTKAZ.html',
                  {'basket': basket, 'form': form})

# Вывод реестра отказов на СЭЗ
class OTKAZListView(ListView, Default_value):  # Возврат листа объектов
    model = OTKItem # определение таблицы для взаимодействия
    template_name = 'orders1/order1/Otkaz_ALL.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'OTKItem'  # Отправка данных по заданному ключу (object_list)
    queryset = OTKItem.objects.filter(product1__Vip=True, otk__vidano="Управление Роспотребнадзора по Архангельской области")
    extra_context = {'title': 'Список отказов'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = OTKItem.objects.order_by('otk')
        context = super(OTKAZListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5

# Вывод реестра отказов на СЗЗ
class OTKAZListViewRESH(ListView, Default_value):  # Возврат листа объектов
    model = OTKItem # определение таблицы для взаимодействия
    template_name = 'orders1/order1/Otkaz_ALL_RESH.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'OTKItem'  # Отправка данных по заданному ключу (object_list)
    queryset = OTKItem.objects.filter(product2__Vip=True, otk__vidano="Управление Роспотребнадзора по Архангельской области")
    extra_context = {'title': 'Список отказов решения'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = OTKItem.objects.order_by('otk')
        context = super(OTKAZListViewRESH, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5
# Create your views here.


