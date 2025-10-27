# receive_transaction/admin.py
from django.contrib import admin
from .models import CashReceive, BankReceive, DealerBankReceive

@admin.register(CashReceive)
class CashReceiveAdmin(admin.ModelAdmin):
    list_display = ['receive_id', 'account_name', 'receive_amount', 'status', 'entry_date']
    list_filter = ['status', 'entry_date']
    search_fields = ['receive_id', 'account_name']

@admin.register(BankReceive)
class BankReceiveAdmin(admin.ModelAdmin):
    list_display = ['receive_id', 'account_name', 'receive_bank_name', 'type', 'amount', 'status']
    list_filter = ['status', 'type', 'entry_date']
    search_fields = ['receive_id', 'account_name']

@admin.register(DealerBankReceive)
class DealerBankReceiveAdmin(admin.ModelAdmin):
    list_display = ['receive_id', 'dealer', 'district', 'type', 'amount', 'status']
    list_filter = ['status', 'type', 'district']
    search_fields = ['receive_id', 'dealer', 'district']