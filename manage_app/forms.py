# manage_app/forms.py
from django import forms
from .models import Product, Godown, Dump, CostCenter

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'product_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Group'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Title'}),
            'title_bengali': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Title Bengali'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Color'}),
            'unit_type': forms.Select(attrs={'class': 'form-control'}),
            'unit_strength': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Product Unit Strength'}),
            'open_sale_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Open Sale Price'}),
            'allotment_sale_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Allotment Sale Price'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class GodownForm(forms.ModelForm):
    class Meta:
        model = Godown
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Godown Name'}),
            'ghat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Godown Ghat'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'sales_hub': forms.Select(attrs={'class': 'form-control'}),
        }

class DumpForm(forms.ModelForm):
    class Meta:
        model = Dump
        fields = '__all__'
        widgets = {
            'godown': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dump Name'}),
        }

class CostCenterForm(forms.ModelForm):
    class Meta:
        model = CostCenter
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cost Center Name'}),
            'entry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }