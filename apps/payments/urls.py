from django.urls import path

from .views import create_payment, payment_list

app_name = 'payments'

urlpatterns = [
    path('', payment_list, name='payment_list'),
    path('create/', create_payment, name='create_payment'),
]