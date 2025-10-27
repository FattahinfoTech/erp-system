# receive_transaction/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cash-receive/', views.cash_receive, name='cash_receive'),
    path('cash-receive-confirm/', views.cash_receive_confirm, name='cash_receive_confirm'),
    path('bank-receive/', views.bank_receive, name='bank_receive'),
    path('dealer-bank-receive/', views.dealer_bank_receive, name='dealer_bank_receive'),
    path('bank-receive-confirm/', views.bank_receive_confirm, name='bank_receive_confirm'),
]