# user_manage/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, UserPermission

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['employee_id', 'phone', 'address', 'role', 'department', 'status']
        widgets = {
            'employee_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class UserPermissionForm(forms.ModelForm):
    class Meta:
        model = UserPermission
        fields = ['module', 'can_view', 'can_create', 'can_edit', 'can_delete', 'can_approve']
        widgets = {
            'module': forms.Select(attrs={'class': 'form-control'}),
            'can_view': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_create': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_edit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_delete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_approve': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }