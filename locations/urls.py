from django.urls import path
from . import views

app_name = 'locations'
urlpatterns = [
    path('test/', views.test,  name='test'),
    path('test/<str:param>', views.test_param, name='test_param'),
]