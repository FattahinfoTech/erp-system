# petty_cash_transaction/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('entry/', views.petty_cash_entry, name='petty_cash_entry'),
    path('audit/', views.petty_cash_audit, name='petty_cash_audit'),
    path('account/', views.petty_cash_account, name='petty_cash_account'),
    path('confirm/', views.petty_cash_confirm, name='petty_cash_confirm'),
]