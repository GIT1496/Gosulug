from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns


from core.views import *
from core.admin import *

urlpatterns = [
    path('', index_template, name='index_library'),
    # path('list/', reestr_template, name='list_reestr'),
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
    # path('core/search/', HomePageView.as_view(), name='home'),
    path('registration/', user_registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    # email
    path('contact/', send_contact_email, name='send_contact'),

    path('api/library/', reestr_api_list, name='api_reestr_list'),
    path('api/library/<int:pk>', reestr_api_detail, name='api_reestr_detail'),
]
