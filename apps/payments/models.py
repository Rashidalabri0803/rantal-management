from django.db import models
from apps.leases.models import Lease

class Payment(models.Model):
    STATUS_CHOICES = (
        ('paid', 'مدفوع'),
        ('partial', 'جزئي'),
        ('late', 'متأخر'),
    )
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='paid')
    receipt = models.FileField(upload_to='payments/', blank=True, null=True)
    remaining_blance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  
    def __str__(self):
        return f"دفع {self.amount} للعقد {self.lease}"