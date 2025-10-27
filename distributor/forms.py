# distributor/forms.py
from django import forms
from .models import MPO, ASM, RSM, SM, Area, RouteAssignment

class MPOForm(forms.ModelForm):
    class Meta:
        model = MPO
        fields = ['name', 'contact']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type MPO Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type MPO Contact'}),
        }

class ASMForm(forms.ModelForm):
    class Meta:
        model = ASM
        fields = ['name', 'mobile', 'asm_code', 'zone_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ASM Name'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'asm_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ASM Code'}),
            'zone_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zone Name'}),
        }

class RSMForm(forms.ModelForm):
    class Meta:
        model = RSM
        fields = ['name', 'contact', 'rsm_code', 'region_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RSM Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RSM Contact'}),
            'rsm_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RSM Code'}),
            'region_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Region Name'}),
        }

class SMForm(forms.ModelForm):
    class Meta:
        model = SM
        fields = ['name', 'contact', 'sm_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type SM Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type SM Contact'}),
            'sm_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type SM Code'}),
        }

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['route_name', 'tr_code', 'district', 'thana', 'post_code', 'location_detail']
        widgets = {
            'route_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Route Name'}),
            'tr_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TR Code'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select District'}),
            'thana': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Thana'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Code'}),
            'location_detail': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Location Detail', 'rows': 3}),
        }

class RouteAssignmentForm(forms.ModelForm):
    class Meta:
        model = RouteAssignment
        fields = ['sm', 'rsm', 'asm', 'mpo', 'route', 'depo']
        widgets = {
            'sm': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Search SM'}),
            'rsm': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Search RSM'}),
            'asm': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Search ASM'}),
            'mpo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Search MPO'}),
            'route': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Search Route'}),
            'depo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search Depo'}),
        }