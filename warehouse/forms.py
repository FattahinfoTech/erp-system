# warehouse/forms.py
from django import forms
from .models import MotherToLighter, LighterToGhat, GhatToDump, Correction, DOChange, Transfer

class MotherToLighterForm(forms.ModelForm):
    class Meta:
        model = MotherToLighter
        fields = '__all__'
        widgets = {
            'lc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type LC Number'}),
            'mother_vessel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Mother Vessel'}),
            'lighter_vessel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lighter Vessel'}),
            'carrying_contractor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Carrying Contractor'}),
            'product_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'arrival_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class LighterToGhatForm(forms.ModelForm):
    class Meta:
        model = LighterToGhat
        fields = '__all__'
        widgets = {
            'lc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type LC Number'}),
            'lighter_vessel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Lighter Vessel'}),
            'product_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Name'}),
            'moving_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'received_godown': forms.Select(attrs={'class': 'form-control'}),
        }

class GhatToDumpForm(forms.ModelForm):
    class Meta:
        model = GhatToDump
        fields = '__all__'
        widgets = {
            'lc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type LC Number'}),
            'godown': forms.Select(attrs={'class': 'form-control'}),
            'lighter_vessel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Lighter Vessel'}),
            'product_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Name'}),
            'update_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type Note', 'rows': 3}),
            'dump': forms.Select(attrs={'class': 'form-control'}),
        }

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'
        widgets = {
            'product_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Name'}),
            'lc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select LC'}),
            'from_godown': forms.Select(attrs={'class': 'form-control'}),
            'from_dump': forms.Select(attrs={'class': 'form-control'}),
            'transfer_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'to_godown': forms.Select(attrs={'class': 'form-control'}),
            'to_dump': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type Note', 'rows': 3}),
        }