# transfer/forms.py
from django import forms
from .models import TransferManage

class TransferManageForm(forms.ModelForm):
    class Meta:
        model = TransferManage
        fields = '__all__'
        exclude = ['transfer_id']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'from_location': forms.Select(attrs={'class': 'form-control'}),
            'to_location': forms.Select(attrs={'class': 'form-control'}),
            'product_type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }