from django.shortcuts import render

# Create your views here.
# reports/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import (
    AccountsReportForm, CashReportForm, SaleReportForm, WarehouseReportForm
)

@login_required
def accounts_report(request):
    if request.method == 'POST':
        form = AccountsReportForm(request.POST)
        if form.is_valid():
            # Process report generation
            return render(request, 'reports/report_output.html', {
                'report_type': 'Accounts Report',
                'parameters': form.cleaned_data
            })
    else:
        form = AccountsReportForm()
    return render(request, 'reports/accounts_report.html', {'form': form})

@login_required
def cash_report(request):
    if request.method == 'POST':
        form = CashReportForm(request.POST)
        if form.is_valid():
            return render(request, 'reports/report_output.html', {
                'report_type': 'Cash Report',
                'parameters': form.cleaned_data
            })
    else:
        form = CashReportForm()
    return render(request, 'reports/cash_report.html', {'form': form})

@login_required
def sale_report(request):
    if request.method == 'POST':
        form = SaleReportForm(request.POST)
        if form.is_valid():
            return render(request, 'reports/report_output.html', {
                'report_type': 'Sale Report',
                'parameters': form.cleaned_data
            })
    else:
        form = SaleReportForm()
    return render(request, 'reports/sale_report.html', {'form': form})

@login_required
def bank_report(request):
    return render(request, 'reports/bank_report.html')

@login_required
def admin_report(request):
    return render(request, 'reports/admin_report.html')

@login_required
def warehouse_report(request):
    if request.method == 'POST':
        form = WarehouseReportForm(request.POST)
        if form.is_valid():
            return render(request, 'reports/report_output.html', {
                'report_type': 'Warehouse Report',
                'parameters': form.cleaned_data
            })
    else:
        form = WarehouseReportForm()
    return render(request, 'reports/warehouse_report.html', {'form': form})

@login_required
def allotment_report(request):
    return render(request, 'reports/allotment_report.html')

@login_required
def journal_report(request):
    return render(request, 'reports/journal_report.html')