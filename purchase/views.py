# purchase/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Supplier, Purchase
from .forms import SupplierForm, PurchaseForm

@login_required
def purchase_create(request):
    purchases = Purchase.objects.filter(status='Pending')
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_create')
    else:
        form = PurchaseForm()
    return render(request, 'purchase/purchase_create.html', {'purchases': purchases, 'form': form})

@login_required
def leaf_purchase_audit(request):
    purchases = Purchase.objects.filter(status='Pending')
    return render(request, 'purchase/leaf_purchase_audit.html', {'purchases': purchases})

@login_required
def leaf_purchase_approve(request):
    purchases = Purchase.objects.filter(status='Approved')
    return render(request, 'purchase/leaf_purchase_approve.html', {'purchases': purchases})

@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'purchase/supplier_list.html', {'suppliers': suppliers, 'form': form})