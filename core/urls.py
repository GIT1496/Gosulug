from django.urls import path

# Автодополнение
from core.autocomplete import MyModelAutocompleteView, ADRRES1AutocompleteView, VIDAutocompleteView, APAutocompleteView
from core.autocomplete import FCADRautocompView, APautocompView, ADRAPautocompView, ACRautocompView, NACRautocompView
from core.autocomplete import DEJautocompView,ADRDESautocompView, ACCRESDautocompView, NAMEautocompView, ADR1autocompView, predprauto

# Views
from core.views import *

# Поиск
from core.search import SearchResultsView, SearchResultsView1, SearchResultsView2, SearchResultsView3, SearchResultsView4, SearchResultsView5
from core.search import SearchResultsView6, SearchResultsView7, SearchResultsView8, SearchResultsView9, SearchResultsView10, SearchResultsView11, SearchResultsView12

# Фильтр
from core import filterssez

urlpatterns = [
 # index
    path('', index_template, name='index_gosuslug'),

# Представления core
    path('core/view/All/', SEZListView.as_view(), name='list_SEZ_view'),
    path('info', ReshenieView.as_view(), name='list_RESH_view'),
    path('add', RESHCreateView.as_view(), name='add_RESH_view'),
    path('detail<int:RES1>/', resh_detail, name='one_Resh'),
    path('core/view/edit/<int:pk>', RESHUpdateView.as_view(), name='edit_Resh_view'),
    path('core/view/add/', SEZCreateView.as_view(), name='add_SEZ_view'),
    path('edit/<int:pk>', SEZUpdateView.as_view(), name='edit_SEZ_view'),
    path('list/<int:SEZ>/', SEZ_detail, name='one_SEZ'),


# Поиск
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search1/', SearchResultsView1.as_view(), name='search_results1'),
    path('search2/', SearchResultsView2.as_view(), name='search_results2'),
    path('search3/', SearchResultsView3.as_view(), name='search_results3'),
    path('search4/', SearchResultsView4.as_view(), name='search_results4'),
    path('search5/', SearchResultsView5.as_view(), name='search_results5'),
    path('search6/', SearchResultsView6.as_view(), name='search_results6'),
    path('search7/', SearchResultsView7.as_view(), name='search_results7'),
    path('search8/', SearchResultsView8.as_view(), name='search_results8'),
    path('search9/', SearchResultsView9.as_view(), name='search_results9'),
    path('search10/', SearchResultsView10.as_view(), name='search_results10'),
    path('search11/', SearchResultsView11.as_view(), name='search_results11'),
    path('search12/', SearchResultsView12.as_view(), name='search_results12'),



# Регистрация и авторизация
    path('registration/', user_registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

 # Автодополнение
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

 # Фильтрация на стороне клиента
    path('filter', filterssez.Reestr1_list, name="SEZ_filter_list"),
    path('filter/<int:pk>', filterssez.Reestr1_filter, name="SEZ_filter"),
    path('filter2/', filterssez.Reestr2_list, name="RESH_filter_list"),
    path('filter2/<int:pk>', filterssez.Reestr2_filter, name="RESH_filter"),


 # email
    path('contact/', send_contact_email, name='send_contact'),

# API
    path('api/library/', reestr_api_list_SEZ, name='api_reestr_list_SEZ'),
    path('api/library/', reestr_api_list_RESH, name='api_reestr_list_RESH'),
]
