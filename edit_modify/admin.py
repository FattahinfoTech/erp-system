# edit_modify/admin.py
from django.contrib import admin
from .models import TransactionEdit

@admin.register(TransactionEdit)
class TransactionEditAdmin(admin.ModelAdmin):
    list_display = ['transaction_type', 'transaction_id', 'updated_by', 'updated_at']
    list_filter = ['transaction_type', 'updated_at']
    search_fields = ['transaction_id', 'updated_by']
    readonly_fields = ['updated_at']