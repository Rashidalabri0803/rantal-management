from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('lease', 'amount', 'payment_date', 'status', 'remainig_balance', 'receipt')
    list_filter = ('status', 'payment_date')
    search_fields = ('lease__tenant__username',)
    readonly_fields = ('payment_date',)