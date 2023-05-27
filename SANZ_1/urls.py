from django.urls import path
from .import views
from SANZ_1.views import *


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('create2/', views.order_create2, name='order_create2'),
    path('create3/', views.order_create3, name='order_create3'),
    path('SANZ/view/All/', SANZListView.as_view(), name='list_SANZ_view'),
    path('resh', RESHListView.as_view(), name='list_SANZ_RESH_view'),
]