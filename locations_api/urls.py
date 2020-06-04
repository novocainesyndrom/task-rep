from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .views import *

app_name = 'locations_api'
urlpatterns = [
    path('countries/', CountriesView.as_view()),
    path('countries/<int:pk>/', CountryView.as_view()),
    path('cities/', CitiesView.as_view()),
    path('cities/<int:pk>/', CityView.as_view()),
    path('create_user/', UserView.as_view()),
    path('tok_obt/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('tok_ref/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('google/', GoogleView.as_view(), name='google'),
]
