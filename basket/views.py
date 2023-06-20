from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from core.models import Reestr_1, Reestr_2
from .basket import Basket
from .basket import Basket_resh
from .forms import BasketAddProductForm
from django.views.decorators.http import require_POST

"""Работа с внесенными заявления внутри сессии"""
@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product_obj = get_object_or_404(Reestr_1, pk=product_id)
    form = BasketAddProductForm(request.POST)
    print(product_id)
    if form.is_valid():
        basket.add(product=product_obj,
                   count_product=form.cleaned_data['count_prod'],
                   update_count=form.cleaned_data['update'])

    return redirect('list_basket_prod')

@require_POST
def basket_add_resh(request, product_id):
    print(product_id)
    basket = Basket_resh(request)
    product_obj = get_object_or_404(Reestr_2, pk=product_id)
    form = BasketAddProductForm(request.POST)
    print(product_id)
    if form.is_valid():
        basket.add(product=product_obj,
                   count_product=form.cleaned_data['count_prod'],
                   update_count=form.cleaned_data['update'])

    return redirect('list_basket_resh')


def basket_remove(request, product_id):
    basket = Basket(request)
    product_obj = get_object_or_404(Reestr_1, pk=product_id)

    basket.remove(product=product_obj)
    return redirect('list_basket_prod')

def basket_remove_resh(request, product_id):
    basket = Basket_resh(request)
    product_obj = get_object_or_404(Reestr_2, pk=product_id)

    basket.remove(product=product_obj)
    return redirect('list_basket_prod')




def basket_info(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})

def basket_info_resh(request):
    basket = Basket_resh(request)
    return render(request, 'basket/detail_resh.html', {'basket': basket})



def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('list_SEZ_view')

def с(request):
    basket = Basket(request)
    basket.clear()
    return redirect('list_RESH_view')



# Create your views here.
