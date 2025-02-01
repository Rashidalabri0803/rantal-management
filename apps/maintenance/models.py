from django.db import models
from apps.properties.models import Unit
from apps.users.models import User

class Maintenance(models.Model):
  MAINTENANCE_TYPE_CHOICES = [
    ('electrical', 'الكهرباء'),
    ('plumbing', 'سباكة'),
    ('general', 'عام'),
  ]

  STATUS_CHOICES = [
    ('pending', 'قيد الانتظار'),
    ('in_progress', 'قيد التنفيذ'),
    ('completed', 'مكتمل'),
  ]

  unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
  tenant = models.ForeignKey(User, on_delete=models.CASCADE)
  maintenance_type = models.CharField(max_length=20, choices=MAINTENANCE_TYPE_CHOICES, default='general')
  description = models.TextField()
  image = models.ImageField(upload_to='maintenance/', blank=True, null=True)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

  def __str__(self):
    return f"طلب {self.get_maintenance_type_display()} - {self.unit}"
