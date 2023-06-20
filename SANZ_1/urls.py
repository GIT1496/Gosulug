from django.urls import path
from .import views
from SANZ_1.views import *

# Автодополнение
from core.autocomplete import SVOBLautocompView, SVVIDLautocompView, SVFIRMLautocompView, SVNORMautocompView, PerprautocompView


urlpatterns = [
    path('create/', views.add_SEZ, name='add_SEZ'),
    path('create2/', views.add_LIC, name='add_LIC'),
    path('create3/', views.add_RESH, name='add_RESH'),
    path('create4/', views.add_SVID, name='add_SVID'),
    path('create5/', views.add_PEREOF, name='add_PEREOF'),
    path('SANZ/view/All/', SANZListView.as_view(), name='list_SANZ_view'),
    path('resh', RESHListView.as_view(), name='list_SANZ_RESH_view'),
    path('OBLautocompView/', SVOBLautocompView.as_view(), name='OBLautocompView'),
    path('SVVID_autocomplete/', SVVIDLautocompView.as_view(), name='SVVID_autocomplete'),
    path('FIRM_autocomplete/', SVFIRMLautocompView.as_view(), name='FIRM_autocomplete'),
    path('NORM_autocomplete/', SVNORMautocompView.as_view(), name='NORM_autocomplete'),
    path('PEREPR_autocomplete/', PerprautocompView.as_view(), name='PEREPR_autocomplete'),

]