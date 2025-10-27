# edit_modify/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('transaction/', views.transaction, name='edit_transaction'),
    path('allotment/', views.allotment, name='edit_allotment'),
]