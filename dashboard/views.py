# dashboard/views.py (updated)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from user_manage.decorators import role_required
from .models import DashboardStats

@login_required
def dashboard(request):
    stats, created = DashboardStats.objects.get_or_create(pk=1)
    
    context = {
        'sales_today': stats.sales_today,
        'sales_week': stats.sales_week,
        'sales_month': stats.sales_month,
        'production_yesterday': stats.production_yesterday,
        'production_week': stats.production_week,
    }
    return render(request, 'dashboard/dashboard.html', context)

# Example of role-based access
@role_required(['Admin', 'Manager'])
def admin_dashboard(request):
    # Special admin dashboard
    return render(request, 'dashboard/admin_dashboard.html')