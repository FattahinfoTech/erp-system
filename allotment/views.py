# allotment/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dealer, AllotmentSale
from .forms import DealerForm, AllotmentSaleForm

@login_required
def sale(request):
    allotments = AllotmentSale.objects.all()
    if request.method == 'POST':
        form = AllotmentSaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allotment_sale')
    else:
        form = AllotmentSaleForm()
    return render(request, 'allotment/sale.html', {'allotments': allotments, 'form': form})

@login_required
def sale_audit(request):
    allotments = AllotmentSale.objects.filter(status='Pending')
    return render(request, 'allotment/sale_audit.html', {'allotments': allotments})

@login_required
def sale_documents(request):
    allotments = AllotmentSale.objects.filter(status='Approved')
    return render(request, 'allotment/sale_documents.html', {'allotments': allotments})

@login_required
def allotment_audit(request):
    return render(request, 'allotment/allotment_audit.html')

@login_required
def dealer_list(request):
    dealers = Dealer.objects.all()
    if request.method == 'POST':
        form = DealerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dealer_list')
    else:
        form = DealerForm()
    return render(request, 'allotment/dealer_list.html', {'dealers': dealers, 'form': form})

@login_required
def allotment(request):
    return render(request, 'allotment/allotment.html')

@login_required
def arrival_receiving(request):
    allotments = AllotmentSale.objects.filter(status='Approved')
    return render(request, 'allotment/arrival_receiving.html', {'allotments': allotments})