# approve/admin.py
from django.contrib import admin
from .models import TransportApprove

@admin.register(TransportApprove)
class TransportApproveAdmin(admin.ModelAdmin):
    list_display = ['invoice_id', 'transport', 'warehouse', 'quantity', 'total', 'status', 'created_at']
    list_filter = ['status', 'transport', 'warehouse', 'created_at']
    search_fields = ['invoice_id', 'transport']
    readonly_fields = ['approved_at']