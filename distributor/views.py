# distributor/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MPO, ASM, RSM, SM, Area, RouteAssignment
from .forms import MPOForm, ASMForm, RSMForm, SMForm, AreaForm, RouteAssignmentForm

@login_required
def mpo_list(request):
    mpos = MPO.objects.all()
    if request.method == 'POST':
        form = MPOForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mpo_list')
    else:
        form = MPOForm()
    return render(request, 'distributor/mpo.html', {'mpos': mpos, 'form': form})

@login_required
def asm_list(request):
    asms = ASM.objects.all()
    if request.method == 'POST':
        form = ASMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asm_list')
    else:
        form = ASMForm()
    return render(request, 'distributor/asm.html', {'asms': asms, 'form': form})

@login_required
def rsm_list(request):
    rsms = RSM.objects.all()
    if request.method == 'POST':
        form = RSMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rsm_list')
    else:
        form = RSMForm()
    return render(request, 'distributor/rsm.html', {'rsms': rsms, 'form': form})

@login_required
def sm_list(request):
    sms = SM.objects.all()
    if request.method == 'POST':
        form = SMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sm_list')
    else:
        form = SMForm()
    return render(request, 'distributor/sm.html', {'sms': sms, 'form': form})

@login_required
def area_list(request):
    areas = Area.objects.all()
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('area_list')
    else:
        form = AreaForm()
    return render(request, 'distributor/area.html', {'areas': areas, 'form': form})

@login_required
def route_list(request):
    assignments = RouteAssignment.objects.all()
    if request.method == 'POST':
        form = RouteAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteAssignmentForm()
    return render(request, 'distributor/route.html', {'assignments': assignments, 'form': form})