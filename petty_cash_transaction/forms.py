# petty_cash_transaction/forms.py
from django import forms
from .models import PettyCash

class PettyCashForm(forms.ModelForm):
    class Meta:
        model = PettyCash
        fields = ['account', 'transaction_type', 'amount', 'note', 'description', 'voucher_number', 'lc_number', 'entry_date']
        widgets = {
            'account': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Account Name'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Note'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'rows': 3}),
            'voucher_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Voucher Number'}),
            'lc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select LC'}),
            'entry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }