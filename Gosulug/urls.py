"""
URL configuration for Gosulug project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from core.views import index_template
from django.conf.urls import handler404
from django.conf.urls import handler400
from django.conf.urls import handler403

# Пути в URL для приложений проекта
urlpatterns = [
    path('', index_template, name='index_gosuslug'),
    path('admin/', admin.site.urls),
    path('core/', include("core.urls")),
    path('basket/', include('basket.urls')),
    path('orders/', include('SANZ_1.urls')),
    path('orders1/', include('OTKAZ.urls')),
    path('dashboard/', include('dashboardgosusl.urls')),
    path('KMS_sotr/', include('KMS_sotr.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Представления для ошибок в проекте
handler404 = "core.views.error_404"
handler400 = "core.views.error_400"
handler403 = "core.views.error_403"