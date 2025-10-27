# sales/forms.py
from django import forms
from .models import Customer, Sale

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['customer_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Customer Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select District'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Area'}),
            'credit_limit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Credit Limit'}),
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
        exclude = ['invoice_id']
        widgets = {
            'sale_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'physical_invoice_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Physical Invoice Number'}),
            'truck_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Truck No'}),
            'reference_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reference No'}),
            'driver_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Driver Name'}),
            'driver_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Driver contact'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }