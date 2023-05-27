from django.shortcuts import render
from django.shortcuts import render
from .models import SEZ1, SEZItem, Reestr_1, Reestr_2,RESHItem


from basket.basket import Basket, Basket_resh

from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .util import Default_value
from .forms import SEZCreateForm,LICCreateForm, RESHCreateForm



def order_create(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = SEZCreateForm(request.POST)
        if form.is_valid():
            SEZ = form.save()
            for item in basket:
                SEZItem.objects.create(SEZ=SEZ,
                                       product=item['SEZ'])
                Reestr_1.objects.filter(namber=item['SEZ']).update(Vip=True)
            # очистка корзины
            basket.clear()
            # # order_create.delay(SEZ.id)
            return render(request, 'orders/order/created.html',
                          {'SEZ': SEZ })
    else:
        form = SEZCreateForm

    return render(request, 'orders/order/create.html',
                  {'basket': basket, 'form': form})

def order_create2(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = LICCreateForm(request.POST)
        if form.is_valid():
            LIC = form.save()
            for item in basket:
                SEZItem.objects.create(LIC=LIC,
                                       product=item['SEZ'])
                Reestr_1.objects.filter(namber=item['SEZ']).update(Vip=True)
            # очистка корзины
            basket.clear()
            # # order_create.delay(SEZ.id)
            return render(request, 'orders/order/created1.html',
                          {'LIC': LIC })
    else:
        form = LICCreateForm

    return render(request, 'orders/order/created1.html',
                  {'basket': basket, 'form': form})

def order_create3(request):
    basket = Basket_resh(request)
    if request.method == 'POST':
        form = RESHCreateForm(request.POST, request.FILES)
        if form.is_valid():
            resh = form.save()
            for item in basket:
                RESHItem.objects.create(resh=resh,
                                       sajav=item['RES1'])
                Reestr_2.objects.filter(namber=item['RES1']).update(Vip=True)
            # очистка корзины
            basket.clear()
            # # order_create.delay(SEZ.id)
            return render(request, 'orders/order/created2.html',
                          {'resh': resh})
    else:
        form = RESHCreateForm

    return render(request, 'orders/order/create1.html',
                  {'basket': basket, 'form': form})


class SANZListView(ListView, Default_value):  # Возврат листа объектов
    model = SEZItem # определение таблицы для взаимодействия
    template_name = 'orders/order/order_All1.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'RESHi'  # Отправка данных по заданному ключу (object_list)
    queryset = SEZItem.objects.filter(product__Vip=True, SEZ__vidano="Управление Роспотребнадзора по Архангельской области")
    extra_context = {'title': 'Список санитарно-эпидемиологических заключений'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = SEZItem.objects.order_by('SEZ')
        context = super(SANZListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5


class RESHListView(ListView, Default_value):  # Возврат листа объектов
    model = RESHItem # определение таблицы для взаимодействия
    template_name = 'orders/order/order-All2.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'RESHItem'  # Отправка данных по заданному ключу (object_list)
    # queryset = SEZItem.objects.filter(sajav__Vip=True, SEZ__vidano="Управление Роспотребнадзора по Архангельской области")
    extra_context = {'title': 'Список выданных решений'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = RESHItem.objects.order_by('resh')
        context = super(RESHListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5



# Create your views here.
