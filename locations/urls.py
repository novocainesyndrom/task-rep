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
    path('add_country/', views.add_country, name='add_country'),
    path('add_city/<int:country_id>', views.add_city, name='add_city'),
    path('edit_country/<int:country_id>', views.edit_country, name='edit_country'),
    path('edit_city/<int:city_id>', views.edit_city, name='edit_city'),
]