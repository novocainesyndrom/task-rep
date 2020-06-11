from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .views import *


urlpatterns = [
    path('countries/', CountriesView.as_view(), name='countries'),
    path('countries/<int:pk>/', CountryView.as_view(), name='country'),
    path('cities/', CitiesView.as_view()),
    path('cities/<int:pk>/', CityView.as_view(), name='city'),
    path('create_user/', UserView.as_view(), name='create_user'),
    path('tok_obt/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('tok_ref/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('google/', GoogleView.as_view(), name='google'),
]
