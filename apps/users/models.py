from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  ROLE_CHOICES = [
    ('admin', 'مشرف'),
    ('tenant', 'مستأجر')
  ]
  role = models.CharField(max_length=10, choices=ROLE_CHOICES)
  phone_number = models.CharField(max_length=15, blank=True, null=True)
  cr_number = models.CharField(max_length=20, blank=True, null=True)
  signature = models.ImageField(upload_to='signature', blank=True, null=True)
  date_joined = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.username