from django.contrib import admin
from .models import Lease

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'unit', 'start_date', 'end_date', 'is_active', 'contract_file')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('tenant__username', 'unit__property__name')
    readonly_fields = ('calculate_registration_fee',)

    def calculate_registration_fee(self, obj):
        return f"{obj.calculate_registration_fee()} ريال عماني"
    calculate_registration_fee.short_description = 'رسوم تسجيل العقد'