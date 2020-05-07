from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'locations'
urlpatterns = [
    path('countries/', views.countries_page,  name='countries_page'),
    path('countries/<int:country_id>', views.country_page,  name='country_page'),
    path('city/<int:city_id>', views.city,  name='city'),
    path('login/', LoginView.as_view(template_name='locations/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('remove/<int:city_id>', views.remove_city, name='remove'),
]
