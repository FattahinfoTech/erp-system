# receive_transaction/forms.py
from django import forms
from .models import CashReceive, BankReceive, DealerBankReceive

class CashReceiveForm(forms.ModelForm):
    class Meta:
        model = CashReceive
        fields = ['account_name', 'receive_amount', 'receive_note', 'description', 'voucher_number', 'entry_date']
        widgets = {
            'account_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Account Name'}),
            'receive_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'receive_note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Note'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'rows': 3}),
            'voucher_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Voucher Number'}),
            'entry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class BankReceiveForm(forms.ModelForm):
    class Meta:
        model = BankReceive
        fields = ['account_name', 'receive_bank_name', 'type', 'amount', 'note', 'description', 'entry_date']
        widgets = {
            'account_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Account Name'}),
            'receive_bank_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bank Name'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Note'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'rows': 3}),
            'entry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class DealerBankReceiveForm(forms.ModelForm):
    class Meta:
        model = DealerBankReceive
        fields = ['district', 'thana', 'dealer', 'receive_bank_name', 'type', 'amount', 'note', 'description']
        widgets = {
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select District'}),
            'thana': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Thana'}),
            'dealer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Dealer'}),
            'receive_bank_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bank Name'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Note'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'rows': 3}),
        }