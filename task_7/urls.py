
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .drf_url import urlpatterns as doc_drf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('locations.urls', namespace='locations')),
    path('api/', include('locations_api.urls', namespace='locations_api')),
    path('api_auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += doc_drf