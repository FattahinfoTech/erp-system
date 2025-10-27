# allotment/admin.py
from django.contrib import admin
from .models import Dealer, AllotmentSale

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ['name', 'district', 'thana', 'dealer_contact', 'status']
    list_filter = ['district', 'status']
    search_fields = ['name', 'district']

@admin.register(AllotmentSale)
class AllotmentSaleAdmin(admin.ModelAdmin):
    list_display = ['allotment_id', 'dealer', 'district', 'month', 'year', 'status']
    list_filter = ['district', 'month', 'year', 'status']
    search_fields = ['allotment_id', 'dealer__name']