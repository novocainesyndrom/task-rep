
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('locations.urls', namespace='locations')),
    path('api/', include('locations_api.urls', namespace='locations_api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
