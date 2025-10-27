# transfer/views.py (updated)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from .models import TransferManage
from .forms import TransferManageForm

@login_required
def transfer_create(request):
    transfers = TransferManage.objects.filter(status='Pending')
    if request.method == 'POST':
        form = TransferManageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transfer_create')
    else:
        form = TransferManageForm()
    return render(request, 'transfer/transfer_create.html', {'transfers': transfers, 'form': form})

@login_required
def transfer_approve(request):
    transfers = TransferManage.objects.filter(status='Pending')
    if request.method == 'POST':
        form = TransferManageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transfer_approve')
    else:
        form = TransferManageForm()
    return render(request, 'transfer/transfer_approve.html', {'transfers': transfers, 'form': form})

@login_required
def transfer_receive(request):
    transfers = TransferManage.objects.filter(status='Approved')
    return render(request, 'transfer/transfer_receive.html', {'transfers': transfers})

@login_required
def approve_transfer(request, transfer_id):
    if request.method == 'POST':
        transfer = get_object_or_404(TransferManage, id=transfer_id)
        transfer.status = 'Approved'
        transfer.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def receive_transfer(request, transfer_id):
    if request.method == 'POST':
        transfer = get_object_or_404(TransferManage, id=transfer_id)
        transfer.status = 'Received'
        transfer.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})