from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'cities', CityView)

app_name = 'locations_api'
urlpatterns = [
    path('countries/', CountriesView.as_view()),
    path('countries/<int:pk>/', CountryView.as_view()),
    path('', include(router.urls)),
]
