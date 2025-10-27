# accounting/admin.py
from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_id', 'account_title', 'ex_type', 'district', 'account_status']
    list_filter = ['ex_type', 'account_status', 'district']
    search_fields = ['account_id', 'account_title', 'contact_number']