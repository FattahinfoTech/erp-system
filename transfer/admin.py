# transfer/admin.py
from django.contrib import admin
from .models import TransferManage

@admin.register(TransferManage)
class TransferManageAdmin(admin.ModelAdmin):
    list_display = ['transfer_id', 'from_location', 'to_location', 'product_type', 'status', 'date']
    list_filter = ['status', 'date', 'product_type']
    search_fields = ['transfer_id']