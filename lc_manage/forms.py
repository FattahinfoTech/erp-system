# lc_manage/forms.py
from django import forms
from .models import Consignee, LC

class ConsigneeForm(forms.ModelForm):
    class Meta:
        model = Consignee
        fields = '__all__'
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Consignee Name'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Consignee Owner Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}),
            'reg_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Consignee Reg Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Consignee Address', 'rows': 3}),
        }

class LCForm(forms.ModelForm):
    class Meta:
        model = LC
        fields = '__all__'
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Name'}),
            'consignee': forms.Select(attrs={'class': 'form-control'}),
            'exporter_info': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Exporter Info', 'rows': 3}),
            'registration_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Registration NO'}),
            'mother_vessel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Mother Vessel'}),
            'lc_bank': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select LC Bank'}),
            'lc_bank_branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type LC Bank Branch'}),
            'exporter_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Exporter Country'}),
            'lc_account': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type LC Account'}),
            'lc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type LC Number'}),
            'allot_lc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Allot LC Number'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Type Unit Price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Type Quantity'}),
            'lc_open_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }