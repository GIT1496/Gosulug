from django.urls import path
from KMS_sotr.views import NSEZListView, NPA_UVEDListView,NPA_SZZListView,NPA_GOSREGListView,NPA_LICENZListView,OPT_STANDListView,ADM_REGListView

"""Диспетчер URL для приложения"""
urlpatterns = [
    path('list/', NSEZListView.as_view(), name='NSEZ'),
    path('list1/', NPA_UVEDListView.as_view(), name='NUV'),
    path('list2/', NPA_SZZListView.as_view(), name='NZZ'),
    path('list3/', NPA_GOSREGListView.as_view(), name='NGOSR'),
    path('list4/', NPA_LICENZListView.as_view(), name='NLIC'),
    path('list5/', OPT_STANDListView.as_view(), name='NOPT'),
    path('list6/', ADM_REGListView.as_view(), name='ADMR'),
]
