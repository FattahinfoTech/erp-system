# edit_modify/forms.py
from django import forms

class SaleUpdateForm(forms.Form):
    sale_id = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Sale ID'})
    )

class PurchaseUpdateForm(forms.Form):
    purchase_id = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Purchase ID'})
    )

class BankUpdateForm(forms.Form):
    bank_id = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Bank ID'})
    )

class CashUpdateForm(forms.Form):
    cash_id = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Cash ID'})
    )

class JournalUpdateForm(forms.Form):
    journal_id = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Journal ID'})
    )

class AllotmentUpdateForm(forms.Form):
    allotment_id = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Allotment ID'})
    )

class AllotmentSearchForm(forms.Form):
    district = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select District'})
    )
    thana = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Thana'})
    )
    lc_number = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select LC'})
    )
    month = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Month'})
    )
    year = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Year'})
    )