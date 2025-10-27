# sales/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('sale-create/', views.sale_create, name='sale_create'),
    path('sale-audit-approve/', views.sale_audit_approve, name='sale_audit_approve'),
    path('sale-approve/', views.sale_approve, name='sale_approve'),
    path('sale-do-print/', views.sale_do_print, name='sale_do_print'),
    path('allotment-do-print/', views.allotment_do_print, name='allotment_do_print'),
    path('due-collect/', views.due_collect, name='due_collect'),
    path('sale-return/', views.sale_return, name='sale_return'),
    path('sale-delivery/', views.sale_delivery, name='sale_delivery'),
    path('sale-do-verify/', views.sale_do_verify, name='sale_do_verify'),
]