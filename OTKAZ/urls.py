from django.urls import path
from .import views
from OTKAZ.views import *
from core.autocomplete import OTKautocompView, OTKISPautocompView

"""URL адресация в приложении"""
urlpatterns = [
    path('create1/', views.add_OTKAZ_SEZ, name='add_OTKAZ_SEZ'),
    path('create2/', views.add_OTKAZ_RESH, name='add_OTKAZ_RESH'),
    path('OTKAZ/view/All/', OTKAZListView.as_view(), name='otkaz_SANZ_view'),
    path('OTKAZ/view/All2/', OTKAZListViewRESH.as_view(), name='otkaz_RESH_view'),
    path('OTKautocompView/', OTKautocompView.as_view(), name='OTKautocompView'),
    path('OTKISPautocompView/', OTKISPautocompView.as_view(), name='OTKISPautocompView'),
]