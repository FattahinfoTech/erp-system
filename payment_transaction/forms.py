# payment_transaction/forms.py
from django import forms
from .models import CashPayment, BankPayment

class CashPaymentForm(forms.ModelForm):
    class Meta:
        model = CashPayment
        fields = ['account_payment_to', 'payment_amount', 'payment_note', 'description', 'voucher_number', 'entry_date']
        widgets = {
            'account_payment_to': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Account Name'}),
            'payment_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'payment_note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Note'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'rows': 3}),
            'voucher_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Voucher Number'}),
            'entry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class BankPaymentForm(forms.ModelForm):
    class Meta:
        model = BankPayment
        fields = ['account_name', 'payment_bank_name', 'type', 'amount', 'note', 'description']
        widgets = {
            'account_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Account Name'}),
            'payment_bank_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bank Name'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Note'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'rows': 3}),
        }