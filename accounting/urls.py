# accounting/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.account_list, name='account_list'),
]