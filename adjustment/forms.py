# adjustment/forms.py
from django import forms
from .models import ProductPlus, ProductMinus

class ProductPlusForm(forms.ModelForm):
    class Meta:
        model = ProductPlus
        fields = ['customer_name', 'entry_date', 'product', 'godown', 'quantity']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Customer Name'}),
            'entry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'godown': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProductMinusForm(forms.ModelForm):
    class Meta:
        model = ProductMinus
        fields = ['customer_name', 'entry_date', 'product', 'godown', 'quantity']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Customer Name'}),
            'entry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'godown': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }