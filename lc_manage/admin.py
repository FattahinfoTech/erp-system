# lc_manage/admin.py
from django.contrib import admin
from .models import Consignee, LC

@admin.register(Consignee)
class ConsigneeAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'owner_name', 'contact', 'reg_number']
    list_filter = ['type']
    search_fields = ['name', 'owner_name']

@admin.register(LC)
class LCAdmin(admin.ModelAdmin):
    list_display = ['lc_number', 'product_name', 'consignee', 'lc_bank', 'quantity', 'total', 'status']
    list_filter = ['status', 'lc_open_date']
    search_fields = ['lc_number', 'product_name']