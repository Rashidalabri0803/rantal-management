from django.db import models
from apps.users.models import User
from apps.properties.models import Unit

class Lease(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    contract_file = models.FileField(upload_to='contracts/', blank=True, null=True)
    landlord_signature = models.ImageField(upload_to='signatures/', blank=True, null=True)
    tenant_signature = models.ImageField(upload_to='signatures/', blank=True, null=True)

    def calculate_registration_fee(self):
      return round((self.unit.rent_price * 12 * 0.03) + 1, 2)

    def __str__(self):
        return f"عقد {self.tenant.username} - {self.unit}"