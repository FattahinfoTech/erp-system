# purchase/forms.py
from django import forms
from .models import Supplier, Purchase

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Supplier Title'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Supplier Contact'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Supplier Address', 'rows': 3}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select District'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Area'}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }