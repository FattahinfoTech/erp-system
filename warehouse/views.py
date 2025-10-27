from django.shortcuts import render

# Create your views here.
# warehouse/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MotherToLighter, LighterToGhat, GhatToDump, LVActivity, Correction, DOChange, Transfer
from .forms import MotherToLighterForm, LighterToGhatForm, GhatToDumpForm, TransferForm

@login_required
def mother_to_lighter(request):
    transfers = MotherToLighter.objects.all()
    if request.method == 'POST':
        form = MotherToLighterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mother_to_lighter')
    else:
        form = MotherToLighterForm()
    return render(request, 'warehouse/mother_to_lighter.html', {'transfers': transfers, 'form': form})

@login_required
def lighter_to_ghat(request):
    transfers = LighterToGhat.objects.all()
    if request.method == 'POST':
        form = LighterToGhatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lighter_to_ghat')
    else:
        form = LighterToGhatForm()
    return render(request, 'warehouse/lighter_to_ghat.html', {'transfers': transfers, 'form': form})

@login_required
def ghat_to_dump(request):
    transfers = GhatToDump.objects.all()
    if request.method == 'POST':
        form = GhatToDumpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ghat_to_dump')
    else:
        form = GhatToDumpForm()
    return render(request, 'warehouse/ghat_to_dump.html', {'transfers': transfers, 'form': form})

@login_required
def lv_activity(request):
    activities = LVActivity.objects.all()
    return render(request, 'warehouse/lv_activity.html', {'activities': activities})

@login_required
def correction(request):
    corrections = Correction.objects.all()
    return render(request, 'warehouse/correction.html', {'corrections': corrections})

@login_required
def do_change(request):
    changes = DOChange.objects.all()
    return render(request, 'warehouse/do_change.html', {'changes': changes})

@login_required
def transfer(request):
    transfers = Transfer.objects.all()
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transfer')
    else:
        form = TransferForm()
    return render(request, 'warehouse/transfer.html', {'transfers': transfers, 'form': form})