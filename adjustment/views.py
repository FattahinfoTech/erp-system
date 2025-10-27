# adjustment/views.py (updated)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ProductPlus, ProductMinus
from .forms import ProductPlusForm, ProductMinusForm

@login_required
def product_plus(request):
    adjustments = ProductPlus.objects.all()
    
    if request.method == 'POST':
        # Handle delete action
        if 'delete_id' in request.POST:
            adjustment = get_object_or_404(ProductPlus, id=request.POST['delete_id'])
            adjustment.delete()
            messages.success(request, f'Adjustment {adjustment.adjustment_id} deleted successfully.')
            return redirect('product_plus')
        
        # Handle edit action
        elif 'customer_name' in request.POST and 'entry_date' in request.POST:
            # This is a simplified edit - in production, you'd want to use a proper edit form
            adjustment_id = request.POST.get('adjustment_id')
            if adjustment_id:
                adjustment = get_object_or_404(ProductPlus, id=adjustment_id)
                adjustment.customer_name = request.POST['customer_name']
                adjustment.entry_date = request.POST['entry_date']
                adjustment.product = request.POST['product']
                adjustment.godown = request.POST['godown']
                adjustment.quantity = request.POST['quantity']
                adjustment.save()
                messages.success(request, f'Adjustment {adjustment.adjustment_id} updated successfully.')
            return redirect('product_plus')
        
        # Handle new creation
        else:
            form = ProductPlusForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product plus adjustment created successfully.')
                return redirect('product_plus')
    else:
        form = ProductPlusForm()
    
    return render(request, 'adjustment/product_plus.html', {'adjustments': adjustments, 'form': form})

@login_required
def product_plus_approve(request):
    adjustments = ProductPlus.objects.filter(status='Pending')
    
    if request.method == 'POST':
        # Handle approve action
        if 'approve_id' in request.POST:
            adjustment = get_object_or_404(ProductPlus, id=request.POST['approve_id'])
            adjustment.status = 'Approved'
            adjustment.save()
            messages.success(request, f'Adjustment {adjustment.adjustment_id} approved successfully.')
            return redirect('product_plus_approve')
        
        # Handle delete action
        elif 'delete_id' in request.POST:
            adjustment = get_object_or_404(ProductPlus, id=request.POST['delete_id'])
            adjustment.delete()
            messages.success(request, f'Adjustment {adjustment.adjustment_id} deleted successfully.')
            return redirect('product_plus_approve')
        
        # Handle new creation
        else:
            form = ProductPlusForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product plus adjustment created successfully.')
                return redirect('product_plus_approve')
    else:
        form = ProductPlusForm()
    
    return render(request, 'adjustment/product_plus_approve.html', {'adjustments': adjustments, 'form': form})

@login_required
def product_minus(request):
    adjustments = ProductMinus.objects.all()
    
    if request.method == 'POST':
        # Handle delete action
        if 'delete_id' in request.POST:
            adjustment = get_object_or_404(ProductMinus, id=request.POST['delete_id'])
            adjustment.delete()
            messages.success(request, f'Adjustment {adjustment.adjustment_id} deleted successfully.')
            return redirect('product_minus')
        
        # Handle edit action
        elif 'customer_name' in request.POST and 'entry_date' in request.POST:
            # This is a simplified edit - in production, you'd want to use a proper edit form
            adjustment_id = request.POST.get('adjustment_id')
            if adjustment_id:
                adjustment = get_object_or_404(ProductMinus, id=adjustment_id)
                adjustment.customer_name = request.POST['customer_name']
                adjustment.entry_date = request.POST['entry_date']
                adjustment.product = request.POST['product']
                adjustment.godown = request.POST['godown']
                adjustment.quantity = request.POST['quantity']
                adjustment.save()
                messages.success(request, f'Adjustment {adjustment.adjustment_id} updated successfully.')
            return redirect('product_minus')
        
        # Handle new creation
        else:
            form = ProductMinusForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product minus adjustment created successfully.')
                return redirect('product_minus')
    else:
        form = ProductMinusForm()
    
    return render(request, 'adjustment/product_minus.html', {'adjustments': adjustments, 'form': form})

@login_required
def product_minus_approve(request):
    adjustments = ProductMinus.objects.filter(status='Pending')
    
    if request.method == 'POST':
        # Handle approve action
        if 'approve_id' in request.POST:
            adjustment = get_object_or_404(ProductMinus, id=request.POST['approve_id'])
            adjustment.status = 'Approved'
            adjustment.save()
            messages.success(request, f'Adjustment {adjustment.adjustment_id} approved successfully.')
            return redirect('product_minus_approve')
        
        # Handle delete action
        elif 'delete_id' in request.POST:
            adjustment = get_object_or_404(ProductMinus, id=request.POST['delete_id'])
            adjustment.delete()
            messages.success(request, f'Adjustment {adjustment.adjustment_id} deleted successfully.')
            return redirect('product_minus_approve')
        
        # Handle new creation
        else:
            form = ProductMinusForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product minus adjustment created successfully.')
                return redirect('product_minus_approve')
    else:
        form = ProductMinusForm()
    
    return render(request, 'adjustment/product_minus_approve.html', {'adjustments': adjustments, 'form': form})