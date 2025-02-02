from django.urls import path

from .views import create_maintenance, maintenance_list

app_name = 'maintenance'

urlpatterns = [
    path('', maintenance_list, name='maintenance_list'),
    path('create/', create_maintenance, name='create_maintenance'),
]