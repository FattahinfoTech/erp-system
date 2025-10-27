# sales/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Customer, Sale
from .forms import CustomerForm, SaleForm

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'sales/customer_list.html', {'customers': customers, 'form': form})

@login_required
def sale_create(request):
    sales = Sale.objects.filter(status='Pending')
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_create')
    else:
        form = SaleForm()
    return render(request, 'sales/sale_create.html', {'sales': sales, 'form': form})

@login_required
def sale_audit_approve(request):
    sales = Sale.objects.filter(status='Pending')
    return render(request, 'sales/sale_audit_approve.html', {'sales': sales})

@login_required
def sale_approve(request):
    sales = Sale.objects.filter(status='Approved')
    return render(request, 'sales/sale_approve.html', {'sales': sales})

@login_required
def sale_do_print(request):
    sales = Sale.objects.filter(status='Approved')
    return render(request, 'sales/sale_do_print.html', {'sales': sales})

@login_required
def due_collect(request):
    return render(request, 'sales/due_collect.html')

@login_required
def sale_return(request):
    sales = Sale.objects.filter(status='Cancelled')
    return render(request, 'sales/sale_return.html', {'sales': sales})

@login_required
def sale_delivery(request):
    sales = Sale.objects.filter(status='Approved')
    return render(request, 'sales/sale_delivery.html', {'sales': sales})

@login_required
def sale_do_verify(request):
    return render(request, 'sales/sale_do_verify.html')

@login_required
def allotment_do_print(request):
    return render(request, 'sales/allotment_do_print.html')