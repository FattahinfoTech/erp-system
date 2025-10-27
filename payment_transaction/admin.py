# payment_transaction/admin.py
from django.contrib import admin
from .models import CashPayment, BankPayment

@admin.register(CashPayment)
class CashPaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'account_payment_to', 'payment_amount', 'status', 'entry_date']
    list_filter = ['status', 'entry_date']
    search_fields = ['payment_id', 'account_payment_to']

@admin.register(BankPayment)
class BankPaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'account_name', 'payment_bank_name', 'type', 'amount', 'status']
    list_filter = ['status', 'type']
    search_fields = ['payment_id', 'account_name']