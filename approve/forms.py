# approve/forms.py
from django import forms
from .models import TransportApprove

class TransportApproveForm(forms.ModelForm):
    class Meta:
        model = TransportApprove
        fields = ['transport', 'warehouse', 'address', 'quantity', 'unit_price']
        widgets = {
            'transport': forms.Select(attrs={'class': 'form-control'}),
            'warehouse': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }