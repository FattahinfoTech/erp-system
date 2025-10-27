# edit_modify/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    SaleUpdateForm, PurchaseUpdateForm, BankUpdateForm, 
    CashUpdateForm, JournalUpdateForm, AllotmentUpdateForm,
    AllotmentSearchForm
)

@login_required
def transaction(request):
    if request.method == 'POST':
        # Handle different form submissions based on which button was clicked
        if 'sale_update' in request.POST:
            sale_form = SaleUpdateForm(request.POST)
            if sale_form.is_valid():
                sale_id = sale_form.cleaned_data['sale_id']
                messages.success(request, f'Sale Info for {sale_id} will be updated')
                return redirect('edit_transaction')
        elif 'purchase_update' in request.POST:
            purchase_form = PurchaseUpdateForm(request.POST)
            if purchase_form.is_valid():
                purchase_id = purchase_form.cleaned_data['purchase_id']
                messages.success(request, f'Purchase Info for {purchase_id} will be updated')
                return redirect('edit_transaction')
        elif 'bank_update' in request.POST:
            bank_form = BankUpdateForm(request.POST)
            if bank_form.is_valid():
                bank_id = bank_form.cleaned_data['bank_id']
                messages.success(request, f'Bank Info for {bank_id} will be updated')
                return redirect('edit_transaction')
        elif 'cash_update' in request.POST:
            cash_form = CashUpdateForm(request.POST)
            if cash_form.is_valid():
                cash_id = cash_form.cleaned_data['cash_id']
                messages.success(request, f'Cash Info for {cash_id} will be updated')
                return redirect('edit_transaction')
        elif 'journal_update' in request.POST:
            journal_form = JournalUpdateForm(request.POST)
            if journal_form.is_valid():
                journal_id = journal_form.cleaned_data['journal_id']
                messages.success(request, f'Journal Info for {journal_id} will be updated')
                return redirect('edit_transaction')
        elif 'allotment_update' in request.POST:
            allotment_form = AllotmentUpdateForm(request.POST)
            if allotment_form.is_valid():
                allotment_id = allotment_form.cleaned_data['allotment_id']
                messages.success(request, f'Allotment Info for {allotment_id} will be updated')
                return redirect('edit_transaction')
    else:
        sale_form = SaleUpdateForm()
        purchase_form = PurchaseUpdateForm()
        bank_form = BankUpdateForm()
        cash_form = CashUpdateForm()
        journal_form = JournalUpdateForm()
        allotment_form = AllotmentUpdateForm()

    context = {
        'sale_form': sale_form,
        'purchase_form': purchase_form,
        'bank_form': bank_form,
        'cash_form': cash_form,
        'journal_form': journal_form,
        'allotment_form': allotment_form,
    }
    return render(request, 'edit_modify/transaction.html', context)

@login_required
def allotment(request):
    if request.method == 'POST':
        form = AllotmentSearchForm(request.POST)
        if form.is_valid():
            # Process the search
            district = form.cleaned_data['district']
            thana = form.cleaned_data['thana']
            lc_number = form.cleaned_data['lc_number']
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            
            messages.success(request, f'Searching for District: {district}, Thana: {thana}, LC: {lc_number}, Month: {month}, Year: {year}')
            return redirect('edit_allotment')
    else:
        form = AllotmentSearchForm()

    return render(request, 'edit_modify/allotment.html', {'form': form})