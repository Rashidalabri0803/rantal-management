from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'phone_number', 'cr_number', 'date_joined')
    list_filter = ('role', 'date_joined')
    search_fields = ('username', 'email', 'phone_number', 'cr_number')
    readonly_fields = ('date_joined',)