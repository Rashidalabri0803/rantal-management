from django.urls import path

from .views import create_lease, generate_lease_pdf, lease_detail, lease_list

app_name = 'leases'

urlpatterns = [
    path('', lease_list, name='lease_list'),
    path('<int:lease_id>/', lease_detail, name='lease_detail'),
    path('create/', create_lease, name='create_lease'),
    path('pdf/<int:lease_id>/pdf/', generate_lease_pdf, name='generate_lease_pdf'),
]