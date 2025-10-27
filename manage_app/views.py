# manage_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Godown, Dump, CostCenter
from .forms import ProductForm, GodownForm, DumpForm, CostCenterForm

@login_required
def product_list(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'manage_app/product_list.html', {'products': products, 'form': form})

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'manage_app/edit_product.html', {'form': form})

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'manage_app/delete_product.html', {'product': product})

@login_required
def godown_list(request):
    godowns = Godown.objects.all()
    if request.method == 'POST':
        form = GodownForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('godown_list')
    else:
        form = GodownForm()
    return render(request, 'manage_app/godown_list.html', {'godowns': godowns, 'form': form})

@login_required
def dump_list(request):
    dumps = Dump.objects.all()
    if request.method == 'POST':
        form = DumpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dump_list')
    else:
        form = DumpForm()
    return render(request, 'manage_app/dump_list.html', {'dumps': dumps, 'form': form})

@login_required
def cost_center_list(request):
    cost_centers = CostCenter.objects.all()
    if request.method == 'POST':
        form = CostCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cost_center_list')
    else:
        form = CostCenterForm()
    return render(request, 'manage_app/cost_center_list.html', {'cost_centers': cost_centers, 'form': form})