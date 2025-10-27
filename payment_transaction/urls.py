# payment_transaction/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cash-payment/', views.cash_payment, name='cash_payment'),
    path('cash-audit/', views.cash_audit, name='cash_audit'),
    path('cash-account/', views.cash_account, name='cash_account'),
    path('cash-confirm/', views.cash_confirm, name='cash_confirm'),
    path('bank-payment/', views.bank_payment, name='bank_payment'),
    path('bank-payment-confirm/', views.bank_payment_confirm, name='bank_payment_confirm'),
]