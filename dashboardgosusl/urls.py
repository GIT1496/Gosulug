from django.urls import path
from .import views, reshdash, SEZdash

"""URL для диаграмм"""
urlpatterns = [
    path('display1/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data/', views.pivot_data, name='pivot_data'),
    path('display2/', views.display_charts, name='display'),
    path('display2/filters', views.filter_options,name='filter_options'),
    path('display2/sajav/<int:year>/kol', views.get_annual_sajav, name='annual_sajav'),
    path('display2/sajav_vip_chart/<int:year>/', views.sajav_vip_chart, name='sajav_vip_chart'),
    path('display2/GMU_1/<int:year>/', views.GMU_1, name='GMU_1'),
    path('display2/vid_chart/<int:year>/', views.vid_chart, name='vid_chart'),
    path('display3/', reshdash.display_charts2, name='display2'),
    path('display3/filters', reshdash.filter_options_resh, name='filter_options2'),
    path('display3/sajav2/<int:year>/kol2', reshdash.get_annual_sajav2, name='annual_sajav2'),
    path('display3/resh/<int:year>/', reshdash.sajav_vip_chart_resh, name='resh_vip'),
    path('display3/RESH/<int:year>/', reshdash.RESH, name='RESH'),
    path('display3/KL/<int:year>/', reshdash.kl, name='kl'),
    path('display4/', SEZdash.display_charts3, name='display3'),
    path('display4/filters', SEZdash.filter_options_sez, name='filter_options3'),
    path('display4/sajav3/<int:year>/kol3', SEZdash.get_SEZ, name='annual_SEZ'),
    path('display4/sajav4/<int:year>/kol4', SEZdash.get_LIC, name='annual_LIC'),
    path('display4/sajav5/<int:year>/kol5', SEZdash.get_SVID, name='annual_SV'),
    path('display4/sajav6/<int:year>/kol6', SEZdash.get_PERE, name='annual_PERE'),


]
