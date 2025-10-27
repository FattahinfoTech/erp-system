# journal/admin.py
from django.contrib import admin
from .models import Journal, JournalEntry

class JournalEntryInline(admin.TabularInline):
    model = JournalEntry
    extra = 1

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['journal_id', 'date', 'voucher_number', 'amount', 'status']
    list_filter = ['status', 'date']
    search_fields = ['journal_id', 'voucher_number']
    inlines = [JournalEntryInline]

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ['journal', 'trn_id', 'account_debit', 'account_credit', 'debit_amount', 'credit_amount']
    list_filter = ['journal']
    search_fields = ['trn_id', 'account_debit', 'account_credit']