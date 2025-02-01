from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  ROLE_CHOICES = [
    ('admin', 'مشرف'),
    ('tenant', 'مستأجر')
  ]
  role = models.CharField(max_length=10, choices=ROLE_CHOICES)
  phone_number = models.CharField(max_length=15, blank=True, null=True)
  address = models.TextField(blank=True, null=True)
  profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.username