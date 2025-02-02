from django.urls import path

from .views import property_detail, property_list

app_name = 'properties'

urlpatterns = [
    path('', property_list, name='property_list'),
    path('<int:property_id>/', property_detail, name='property_detail'),
]