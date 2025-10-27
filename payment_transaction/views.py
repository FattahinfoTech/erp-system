# payment_transaction/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CashPayment, BankPayment
from .forms import CashPaymentForm, BankPaymentForm

@login_required
def cash_payment(request):
    payments = CashPayment.objects.filter(status='Pending')
    if request.method == 'POST':
        form = CashPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cash_payment')
    else:
        form = CashPaymentForm()
    return render(request, 'payment_transaction/cash_payment.html', {'payments': payments, 'form': form})

@login_required
def cash_audit(request):
    payments = CashPayment.objects.filter(status='Pending')
    return render(request, 'payment_transaction/cash_audit.html', {'payments': payments})

@login_required
def cash_account(request):
    payments = CashPayment.objects.filter(status='Audited')
    return render(request, 'payment_transaction/cash_account.html', {'payments': payments})

@login_required
def cash_confirm(request):
    payments = CashPayment.objects.filter(status='Confirmed')
    return render(request, 'payment_transaction/cash_confirm.html', {'payments': payments})

@login_required
def bank_payment(request):
    payments = BankPayment.objects.filter(status='Pending')
    if request.method == 'POST':
        form = BankPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank_payment')
    else:
        form = BankPaymentForm()
    return render(request, 'payment_transaction/bank_payment.html', {'payments': payments, 'form': form})

@login_required
def bank_payment_confirm(request):
    payments = BankPayment.objects.filter(status='Confirmed')
    return render(request, 'payment_transaction/bank_payment_confirm.html', {'payments': payments})