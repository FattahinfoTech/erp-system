# approve/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import TransportApprove
from .forms import TransportApproveForm

@login_required
def transport_approve(request):
    transports = TransportApprove.objects.filter(status='Pending')
    
    if request.method == 'POST':
        form = TransportApproveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transport_approve')
    else:
        form = TransportApproveForm()

    # Search functionality
    transport_filter = request.GET.get('transport', '')
    warehouse_filter = request.GET.get('warehouse', '')
    
    if transport_filter:
        transports = transports.filter(transport=transport_filter)
    if warehouse_filter:
        transports = transports.filter(warehouse=warehouse_filter)

    context = {
        'transports': transports,
        'form': form,
        'transport_filter': transport_filter,
        'warehouse_filter': warehouse_filter,
    }
    return render(request, 'approve/transport_approve.html', context)

@login_required
def transport_history(request):
    transports = TransportApprove.objects.filter(status='Approved')
    return render(request, 'approve/transport_history.html', {'transports': transports})

@login_required
def approve_transport(request, pk):
    transport = TransportApprove.objects.get(pk=pk)
    transport.status = 'Approved'
    transport.approved_at = timezone.now()
    transport.save()
    return redirect('transport_approve')