from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'countries', CountryView)

app_name = 'locations_api'
urlpatterns = [
    path('', include(router.urls)),
]
