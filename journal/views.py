# journal/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Journal, JournalEntry
from .forms import JournalForm, JournalEntryForm

@login_required
def journal_list(request):
    journals = Journal.objects.all()
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save()
            return redirect('journal_list')
    else:
        form = JournalForm()
    return render(request, 'journal/journal_list.html', {'journals': journals, 'form': form})

@login_required
def journal_approve(request):
    journals = Journal.objects.filter(status='Pending')
    return render(request, 'journal/journal_approve.html', {'journals': journals})

@login_required
def journal_print(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    entries = journal.entries.all()
    total_debit = entries.aggregate(total=Sum('debit_amount'))['total'] or 0
    total_credit = entries.aggregate(total=Sum('credit_amount'))['total'] or 0
    
    context = {
        'journal': journal,
        'entries': entries,
        'total_debit': total_debit,
        'total_credit': total_credit,
    }
    return render(request, 'journal/journal_print.html', context)

@login_required
def journal_details(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    entries = journal.entries.all()
    
    if request.method == 'POST':
        entry_form = JournalEntryForm(request.POST)
        if entry_form.is_valid():
            entry = entry_form.save(commit=False)
            entry.journal = journal
            entry.save()
            
            # Update journal amount
            total_amount = journal.entries.aggregate(total=Sum('debit_amount'))['total'] or 0
            journal.amount = total_amount
            journal.save()
            
            return redirect('journal_details', pk=pk)
    else:
        entry_form = JournalEntryForm()
    
    context = {
        'journal': journal,
        'entries': entries,
        'entry_form': entry_form,
    }
    return render(request, 'journal/journal_details.html', context)