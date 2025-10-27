# settings_app/forms.py
from django import forms
from .models import ClusterZone, FinishProductType, CustomerCategory, EmailSetting

class ClusterZoneForm(forms.ModelForm):
    class Meta:
        model = ClusterZone
        fields = '__all__'
        widgets = {
            'cluster': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cluster'}),
            'zone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zone'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class FinishProductTypeForm(forms.ModelForm):
    class Meta:
        model = FinishProductType
        fields = '__all__'
        widgets = {
            'type_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Title'}),
            'value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Value'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class CustomerCategoryForm(forms.ModelForm):
    class Meta:
        model = CustomerCategory
        fields = '__all__'
        widgets = {
            'category_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Title'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class EmailSettingForm(forms.ModelForm):
    class Meta:
        model = EmailSetting
        fields = '__all__'
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'emails': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Send To Email', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }