from django.contrib import admin

# Register your models here.
# sales/admin.py
from django.contrib import admin
from .models import Customer, Sale

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'name', 'contact', 'district', 'credit_limit', 'status']
    list_filter = ['district', 'status']
    search_fields = ['customer_id', 'name', 'contact']

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['invoice_id', 'customer', 'sale_date', 'truck_number', 'status']
    list_filter = ['status', 'sale_date']
    search_fields = ['invoice_id', 'customer__name', 'truck_number']