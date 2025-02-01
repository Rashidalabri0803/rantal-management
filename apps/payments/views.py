from rest_framework import viewsets
from .models import Payment
from payments.serialisers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer