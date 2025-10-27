# petty_cash_transaction/admin.py
from django.contrib import admin
from .models import PettyCash

@admin.register(PettyCash)
class PettyCashAdmin(admin.ModelAdmin):
    list_display = ['petty_cash_id', 'account', 'transaction_type', 'amount', 'status', 'entry_date']
    list_filter = ['status', 'transaction_type', 'entry_date']
    search_fields = ['petty_cash_id', 'account']