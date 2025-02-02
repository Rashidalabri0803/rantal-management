from django.contrib import admin
from .models import Property, Unit

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'cr_number', 'status', 'manager')
    list_filter = ('status',)
    search_fields = ('name', 'address', 'cr_number')
    readonly_fields = ('cr_number',)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_type', 'property', 'rent_price', 'is_furnished', 'last_updated')
    list_filter = ('unit_type', 'is_furnished')
    search_fields = ('property__name',)