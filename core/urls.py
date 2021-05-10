from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html")),
    path('', include('django.contrib.auth.urls')),
    path('OPAL/', include('OPAL.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT);