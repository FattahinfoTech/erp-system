# adjustment/admin.py
from django.contrib import admin
from .models import ProductPlus, ProductMinus

@admin.register(ProductPlus)
class ProductPlusAdmin(admin.ModelAdmin):
    list_display = ['adjustment_id', 'customer_name', 'product', 'quantity', 'status', 'entry_date']
    list_filter = ['status', 'entry_date']
    search_fields = ['adjustment_id', 'customer_name']

@admin.register(ProductMinus)
class ProductMinusAdmin(admin.ModelAdmin):
    list_display = ['adjustment_id', 'customer_name', 'product', 'quantity', 'status', 'entry_date']
    list_filter = ['status', 'entry_date']
    search_fields = ['adjustment_id', 'customer_name']