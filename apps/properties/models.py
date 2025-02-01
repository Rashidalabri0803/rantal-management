from django.db import models
from users.models import CustomUser

class Property(models.Model):
  TYPE_CHOICES = [
    ('apartment', 'شقة'),
    ('office', 'مكتب'),
    ('shop', 'محل'),
  ]
  name = models.CharField(max_length=100)
  property_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
  location = models.CharField(max_length=255, blank=True, null=True)
  image = models.ImageField(upload_to='properties/', blank=True, null=True)

  def __str__(self):
    return self.name

class Lease(models.Model):
  STATUS_CHOICES = (
    ('active', 'ساري'),
    ('expired', 'منتهي'),
    ('cancelled', 'ملغى'),
  )
  PAYMENT_METHODS = (
    ('bank_transfer', 'تحويل بنكي'),
    ('cash', 'كاش'),
    ('credit_card', 'بطاقة ائتمانية'),
  )
  property = models.OneToOneField(Property, on_delete=models.CASCADE)
  tenant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'tenant'})
  rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
  start_date = models.DateField()
  end_date = models.DateField()
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
  security_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='bank_transfer')

  def __str__(self):
    return f"{self.property.name} - {self.tenant.username}"