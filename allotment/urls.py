# allotment/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('sale/', views.sale, name='allotment_sale'),
    path('sale-audit/', views.sale_audit, name='sale_audit'),
    path('sale-documents/', views.sale_documents, name='sale_documents'),
    path('allotment-audit/', views.allotment_audit, name='allotment_audit'),
    path('dealers/', views.dealer_list, name='dealer_list'),
    path('allotment/', views.allotment, name='allotment'),
    path('arrival-receiving/', views.arrival_receiving, name='arrival_receiving'),
]