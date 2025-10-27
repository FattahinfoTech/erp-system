# journal/forms.py
from django import forms
from .models import Journal, JournalEntry

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['date', 'voucher_number', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'voucher_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Voucher Number'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type Description', 'rows': 3}),
        }

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['trn_id', 'account_debit', 'account_credit', 'lc_number', 'note', 'debit_amount', 'credit_amount']
        widgets = {
            'trn_id': forms.TextInput(attrs={'class': 'form-control'}),
            'account_debit': forms.TextInput(attrs={'class': 'form-control'}),
            'account_credit': forms.TextInput(attrs={'class': 'form-control'}),
            'lc_number': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'debit_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'credit_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }