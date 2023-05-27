from django.urls import path
from .import views
from OTKAZ.views import *


urlpatterns = [
    path('create1/', views.order_create1, name='order_create1'),
    path('create2/', views.order_create_resh, name='order_create_resh'),
    path('OTKAZ/view/All/', OTKAZListView.as_view(), name='otkaz_SANZ_view'),
]