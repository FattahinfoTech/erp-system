# allotment/forms.py
from django import forms
from .models import Dealer, AllotmentSale

class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Dealer Name'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select District'}),
            'thana': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Thana'}),
            'dealer_registration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dealer Registration'}),
            'dealer_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dealer Contact'}),
            'dealer_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dealer Address', 'rows': 3}),
        }

class AllotmentSaleForm(forms.ModelForm):
    class Meta:
        model = AllotmentSale
        fields = '__all__'
        exclude = ['allotment_id']
        widgets = {
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select District'}),
            'thana': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Thana'}),
            'dealer': forms.Select(attrs={'class': 'form-control'}),
            'lc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select LC'}),
            'product_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Product'}),
            'month': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Month'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Year'}),
            'agri_ir': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AGRI/IR'}),
            'agri_ir_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'balance_qty_in_bag': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Balance Quantity In Bag'}),
            'sale_qty_in_bag': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Sale Quantity In Bag'}),
            'm_ton': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'M Ton'}),
            'quantity_in_m_ton': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity In M Ton'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unit Price'}),
            'delivery_product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Delivery Product'}),
            'delivery_from': forms.Select(attrs={'class': 'form-control'}),
            'godown': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Delivery Godown'}),
            'status_type': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }