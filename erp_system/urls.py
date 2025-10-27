# erp_system/urls.py (updated)
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from user_manage.views_auth import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    
    # App URLs
    path('dashboard/', include('dashboard.urls')),
    path('manage/', include('manage_app.urls')),
    path('lc-manage/', include('lc_manage.urls')),
    path('purchase/', include('purchase.urls')),
    path('journal/', include('journal.urls')),
    path('accounting/', include('accounting.urls')),
    path('warehouse/', include('warehouse.urls')),
    path('allotment/', include('allotment.urls')),
    path('adjustment/', include('adjustment.urls')),
    path('settings/', include('settings_app.urls')),
    path('sales/', include('sales.urls')),
    path('transfer/', include('transfer.urls')),
    path('edit-modify/', include('edit_modify.urls')),
    path('receive-transaction/', include('receive_transaction.urls')),
    path('payment-transaction/', include('payment_transaction.urls')),
    path('petty-cash/', include('petty_cash_transaction.urls')),
    path('reports/', include('reports.urls')),
    path('approve/', include('approve.urls')),
    path('user-manage/', include('user_manage.urls')),
    path('distributor/', include('distributor.urls')),
    
    # Redirect root to dashboard
    path('', RedirectView.as_view(url='/dashboard/')),
]