from django.urls import path

from .views import *


urlpatterns = [
    path('',basket_info, name='list_basket_prod'),
    path('info',basket_info_resh, name='list_basket_resh'),
    path('add/<product_id>', basket_add, name='add_basket_1'),
    # path('add/<product_id>', basket_add_1, name='add_basket_1'),
    path('add/resh/<product_id>', basket_add_resh, name='add_basket_2'),
    path('remove/<int:product_id>', basket_remove, name='remove_basket_prod'),
    path('remove/<int:product_id>', basket_remove_resh, name='remove_basket_resh'),
    path('clear/', basket_clear, name='clear_basket_prod'),
]






