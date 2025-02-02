from django.contrib import admin
from .models import Maintenance

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('unit', 'tenant', 'maintenance_type', 'status', 'image')
    list_filter = ('status', 'maintenance_type')
    search_fields = ('unit__property__name', 'tenant__username')
    readonly_fields = ('status',)