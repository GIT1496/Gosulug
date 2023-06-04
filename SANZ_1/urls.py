from django.urls import path
from .import views
from SANZ_1.views import *


urlpatterns = [
    path('create/', views.add_SEZ, name='add_SEZ'),
    path('create2/', views.add_LIC, name='add_LIC'),
    path('create3/', views.add_RESH, name='add_RESH'),
    path('create4/', views.add_SVID, name='add_SVID'),
    path('create5/', views.add_PEREOF, name='add_PEREOF'),
    path('SANZ/view/All/', SANZListView.as_view(), name='list_SANZ_view'),
    path('resh', RESHListView.as_view(), name='list_SANZ_RESH_view'),
]