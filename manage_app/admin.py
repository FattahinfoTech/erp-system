# manage_app/admin.py
from django.contrib import admin
from .models import Product, Godown, Dump, CostCenter

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'product_group', 'unit_type', 'open_sale_price', 'status']
    list_filter = ['category', 'status']
    search_fields = ['title', 'title_bengali']

@admin.register(Godown)
class GodownAdmin(admin.ModelAdmin):
    list_display = ['name', 'ghat', 'type', 'sales_hub', 'contact_number']
    list_filter = ['type', 'sales_hub']
    search_fields = ['name', 'ghat']

@admin.register(Dump)
class DumpAdmin(admin.ModelAdmin):
    list_display = ['name', 'godown', 'created_at']
    list_filter = ['godown']
    search_fields = ['name']

@admin.register(CostCenter)
class CostCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'entry_date', 'status']
    list_filter = ['status']
    search_fields = ['name']