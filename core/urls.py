from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('OPAL/', include('OPAL.urls', namespace="OPAL")),
    path('services/', include('services.urls', namespace="services")),
    path('', include('navigation.urls', namespace="navigation")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT);