# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.accounts_report, name='accounts_report'),
    path('cash/', views.cash_report, name='cash_report'),
    path('sale/', views.sale_report, name='sale_report'),
    path('bank/', views.bank_report, name='bank_report'),
    path('admin/', views.admin_report, name='admin_report'),
    path('warehouse/', views.warehouse_report, name='warehouse_report'),
    path('allotment/', views.allotment_report, name='allotment_report'),
    path('journal/', views.journal_report, name='journal_report'),
]