# accounting/forms.py
from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        widgets = {
            'ex_type': forms.Select(attrs={'class': 'form-control'}),
            'account_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account ID'}),
            'account_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Title'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select District'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Area'}),
            'account_status': forms.Select(attrs={'class': 'form-control'}),
        }