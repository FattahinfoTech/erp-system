# petty_cash_transaction/views.py (updated)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Q
from .models import PettyCash
from .forms import PettyCashForm

@login_required
def petty_cash_entry(request):
    petty_cash_list = PettyCash.objects.all()
    
    if request.method == 'POST':
        if 'delete_id' in request.POST:
            # Handle delete
            petty_cash_id = request.POST.get('delete_id')
            petty_cash = get_object_or_404(PettyCash, id=petty_cash_id)
            petty_cash.delete()
            messages.success(request, 'Petty cash entry deleted successfully!')
            return redirect('petty_cash_entry')
        else:
            # Handle create/update
            form = PettyCashForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Petty cash entry saved successfully!')
                return redirect('petty_cash_entry')
            else:
                messages.error(request, 'Please correct the errors below.')
    else:
        form = PettyCashForm()
    
    return render(request, 'petty_cash_transaction/petty_cash_entry.html', {
        'petty_cash_list': petty_cash_list,
        'form': form
    })

@login_required
def petty_cash_audit(request):
    petty_cash_list = PettyCash.objects.filter(status='Pending')
    
    if request.method == 'POST':
        if 'approve_id' in request.POST:
            petty_cash_id = request.POST.get('approve_id')
            petty_cash = get_object_or_404(PettyCash, id=petty_cash_id)
            petty_cash.status = 'Audited'
            petty_cash.save()
            messages.success(request, 'Petty cash entry approved for audit!')
        elif 'reject_id' in request.POST:
            petty_cash_id = request.POST.get('reject_id')
            petty_cash = get_object_or_404(PettyCash, id=petty_cash_id)
            petty_cash.delete()
            messages.success(request, 'Petty cash entry rejected and deleted!')
    
    return render(request, 'petty_cash_transaction/petty_cash_audit.html', {
        'petty_cash_list': petty_cash_list
    })

@login_required
def petty_cash_account(request):
    petty_cash_list = PettyCash.objects.filter(status='Audited')
    
    # Calculate totals
    total_debit = petty_cash_list.filter(transaction_type='Debit').aggregate(
        total=Sum('amount')
    )['total'] or 0
    
    total_credit = petty_cash_list.filter(transaction_type='Credit').aggregate(
        total=Sum('amount')
    )['total'] or 0
    
    net_balance = total_credit - total_debit
    
    if request.method == 'POST' and 'confirm_id' in request.POST:
        petty_cash_id = request.POST.get('confirm_id')
        petty_cash = get_object_or_404(PettyCash, id=petty_cash_id)
        petty_cash.status = 'Confirmed'
        petty_cash.save()
        messages.success(request, 'Petty cash entry confirmed!')
        return redirect('petty_cash_account')
    
    return render(request, 'petty_cash_transaction/petty_cash_account.html', {
        'petty_cash_list': petty_cash_list,
        'total_debit': total_debit,
        'total_credit': total_credit,
        'net_balance': net_balance
    })

@login_required
def petty_cash_confirm(request):
    petty_cash_list = PettyCash.objects.filter(status='Confirmed')
    return render(request, 'petty_cash_transaction/petty_cash_confirm.html', {
        'petty_cash_list': petty_cash_list
    })