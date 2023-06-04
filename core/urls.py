from django.urls import include, re_path
from django.urls import path
from controlcenter.views import controlcenter
from core.autocomplete import MyModelAutocompleteView, ADRRES1AutocompleteView, VIDAutocompleteView, APAutocompleteView
from core.autocomplete import FCADRautocompView, APautocompView, ADRAPautocompView, ACRautocompView, NACRautocompView
from core.autocomplete import DEJautocompView,ADRDESautocompView, ACCRESDautocompView, NAMEautocompView, ADR1autocompView
# from rest_framework.urlpatterns import format_suffix_patterns
from core.views import *
from core.search import SearchResultsView, SearchResultsView1, SearchResultsView2, SearchResultsView3
from core import filterssez

urlpatterns = [
    path('', index_template, name='index_library'),
    # path('list/', reestr_template, name='list_reestr'),
    # path('test', home, name="home"),
    path('core/view/All/', SEZListView.as_view(), name='list_SEZ_view'),
    path('info', ReshenieView.as_view(), name='list_RESH_view'),
    path('add', RESHCreateView.as_view(), name='add_RESH_view'),
    path('detail<int:RES1>/', resh_detail, name='one_Resh'),
    path('core/view/edit/<int:pk>', RESHUpdateView.as_view(), name='edit_Resh_view'),
    # path('core/view/<int:object_id>', SEZDetailView.as_view(), name='info_SEZ_view'),
    path('core/view/add/', SEZCreateView.as_view(), name='add_SEZ_view'),
    path('edit/<int:pk>', SEZUpdateView.as_view(), name='edit_SEZ_view'),
    path('list/<int:SEZ>/', SEZ_detail, name='one_SEZ'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search1/', SearchResultsView1.as_view(), name='search_results1'),
    path('search2/', SearchResultsView2.as_view(), name='search_results2'),
    path('search3/', SearchResultsView3.as_view(), name='search_results3'),
    # path('core/search/', HomePageView.as_view(), name='home'),
    path('registration/', user_registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('my-model-autocomplete/', MyModelAutocompleteView.as_view(), name='my_model_autocomplete'),
    path('ADRRES1-autocomplete/', ADRRES1AutocompleteView.as_view(), name='ADRRES1_autocomplete'),
    path('VIDA-autocomplete/', VIDAutocompleteView.as_view(), name='VIDA_autocomplete'),
    path('AP-autocomplete/', APAutocompleteView.as_view(), name='AP_autocomplete'),
    path('FC-autocomplete/', FCADRautocompView.as_view(), name='FC_autocomplete'),
    path('APRE-autocomplete/', APautocompView.as_view(), name='APRE_autocomplete'),
    path('ADRAPautocompView/', ADRAPautocompView.as_view(), name='ADRAPautocompView'),
    path('ACRautocompView/', ACRautocompView.as_view(), name='ACRautocompView'),
    path('NACRautocompView/', NACRautocompView.as_view(), name='NACRautocompView'),
    path('DEJautocompView/', DEJautocompView.as_view(), name='DEJautocompView'),
    path('ADRDESautocompView/', ADRDESautocompView.as_view(), name='ADRDESautocompView'),
    path('ACCRESDautocompView/', ACCRESDautocompView.as_view(), name='ACCRESDautocompView'),
    path('ANAMEautocompView/', NAMEautocompView.as_view(), name='NAMEautocompView'),
    path('ADR1autocompView/', ADR1autocompView.as_view(), name='ADR1autocompView'),
    path('filter', filterssez.Reestr1_list, name="SEZ_filter_list"),
    path('filter/<int:pk>', filterssez.Reestr1_filter, name="SEZ_filter"),
    path('filter2/', filterssez.Reestr2_list, name="RESH_filter_list"),
    path('filter2/<int:pk>', filterssez.Reestr2_filter, name="RESH_filter"),


    # email
    path('contact/', send_contact_email, name='send_contact'),

    path('api/library/', reestr_api_list, name='api_reestr_list'),
    path('api/library/<int:pk>', reestr_api_detail, name='api_reestr_detail'),
]
