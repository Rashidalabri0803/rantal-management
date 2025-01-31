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

  def __str__(self):
    return self.name

class Lease(models.Model):
  property = models.OneToOneField(Property, on_delete=models.CASCADE)
  tenant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'tenant'})
  rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
  start_date = models.DateField()
  end_date = models.DateField()

  def __str__(self):
    return f"{self.property.name} - {self.tenant.username}"