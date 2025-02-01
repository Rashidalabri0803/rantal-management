from django.db import models
from properties.models import Lease

class Payment(models.Model):
    STATUS_CHOICES = (
        ('paid', 'مدفوع'),
        ('pending', 'قيد التحقق'),
        ('partial', 'مدفوع بشكل جزئي'),
    )
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)

    def __str__(self):
        return f"{self.lease.property.name} - {self.amount} - {'مدفوع' if self.is_paid else 'غير مدفوع'}"