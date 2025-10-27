from django.shortcuts import render

# Create your views here.
# accounting/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Account
from .forms import AccountForm

@login_required
def account_list(request):
    accounts = Account.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    ex_type_filter = request.GET.get('ex_type', '')
    status_filter = request.GET.get('status', '')
    
    if search_query:
        accounts = accounts.filter(
            Q(account_id__icontains=search_query) |
            Q(account_title__icontains=search_query) |
            Q(contact_number__icontains=search_query)
        )
    
    if ex_type_filter:
        accounts = accounts.filter(ex_type=ex_type_filter)
    
    if status_filter:
        accounts = accounts.filter(account_status=status_filter)
    
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    
    context = {
        'accounts': accounts,
        'form': form,
        'search_query': search_query,
        'ex_type_filter': ex_type_filter,
        'status_filter': status_filter,
    }
    return render(request, 'accounting/account_list.html', context)