from django.db import models
from apps.users.models import User

class Property(models.Model):
  STATUS_CHOICES = [
    ('available', 'متاح'),
    ('unavailable', 'غير متاح'),
    ('under_maintenance', 'تحت الصيانة')
  ]

  name = models.CharField(max_length=255)
  address = models.TextField()
  description = models.TextField(blank=True, null=True)
  cr_number = models.CharField(max_length=20, blank=True, null=True)
  manager = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
  image = models.ImageField(upload_to='properties', blank=True, null=True)
  documents = models.FileField(upload_to='properties_docs', blank=True, null=True)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

  def __str__(self):
    return self.name

class Unit(models.Model):
  UNIT_TYPE_CHOICES = [
    ('apartment', 'شقة'),
    ('office', 'مكتب'),
    ('shop', 'محل'),
  ]

  property = models.ForeignKey('properties.Property', on_delete=models.CASCADE)
  unit_type = models.CharField(max_length=10, choices=UNIT_TYPE_CHOICES)
  rent_price = models.DecimalField(max_digits=10, decimal_places=2)
  is_furnished = models.BooleanField(default=False)
  before_images = models.ImageField(upload_to='units/before/', blank=True, null=True)
  after_images = models.ImageField(upload_to='units/after/', blank=True, null=True)
  last_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.get_unit_type_display()} - {self.property.name}"