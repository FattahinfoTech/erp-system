# lc_manage/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Consignee, LC
from .forms import ConsigneeForm, LCForm

@login_required
def consignee_list(request):
    consignees = Consignee.objects.all()
    if request.method == 'POST':
        form = ConsigneeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consignee_list')
    else:
        form = ConsigneeForm()
    return render(request, 'lc_manage/consignee_list.html', {'consignees': consignees, 'form': form})

@login_required
def lc_list(request):
    lcs = LC.objects.all()
    if request.method == 'POST':
        form = LCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lc_list')
    else:
        form = LCForm()
    return render(request, 'lc_manage/lc_list.html', {'lcs': lcs, 'form': form})

@login_required
def update_lc(request, pk):
    lc = get_object_or_404(LC, pk=pk)
    if request.method == 'POST':
        form = LCForm(request.POST, instance=lc)
        if form.is_valid():
            form.save()
            return redirect('lc_list')
    else:
        form = LCForm(instance=lc)
    return render(request, 'lc_manage/update_lc.html', {'form': form, 'lc': lc})