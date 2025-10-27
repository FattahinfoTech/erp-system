# purchase/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.purchase_create, name='purchase_create'),
    path('audit/', views.leaf_purchase_audit, name='leaf_purchase_audit'),
    path('approve/', views.leaf_purchase_approve, name='leaf_purchase_approve'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
]