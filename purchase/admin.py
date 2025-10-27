# purchase/admin.py
from django.contrib import admin
from .models import Supplier, Purchase

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'district', 'area']
    search_fields = ['name', 'district']

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['purchase_id', 'supplier', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['purchase_id', 'supplier__name']