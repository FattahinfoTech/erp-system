# receive_transaction/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CashReceive, BankReceive, DealerBankReceive
from .forms import CashReceiveForm, BankReceiveForm, DealerBankReceiveForm

@login_required
def cash_receive(request):
    receives = CashReceive.objects.filter(status='Pending')
    if request.method == 'POST':
        form = CashReceiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cash_receive')
    else:
        form = CashReceiveForm()
    return render(request, 'receive_transaction/cash_receive.html', {'receives': receives, 'form': form})

@login_required
def cash_receive_confirm(request):
    receives = CashReceive.objects.filter(status='Confirmed')
    return render(request, 'receive_transaction/cash_receive_confirm.html', {'receives': receives})

@login_required
def bank_receive(request):
    receives = BankReceive.objects.all()
    if request.method == 'POST':
        form = BankReceiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank_receive')
    else:
        form = BankReceiveForm()
    return render(request, 'receive_transaction/bank_receive.html', {'receives': receives, 'form': form})

@login_required
def dealer_bank_receive(request):
    receives = DealerBankReceive.objects.all()
    if request.method == 'POST':
        form = DealerBankReceiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dealer_bank_receive')
    else:
        form = DealerBankReceiveForm()
    return render(request, 'receive_transaction/dealer_bank_receive.html', {'receives': receives, 'form': form})

@login_required
def bank_receive_confirm(request):
    receives = BankReceive.objects.filter(status='Confirmed')
    return render(request, 'receive_transaction/bank_receive_confirm.html', {'receives': receives})