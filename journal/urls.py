# journal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal_list, name='journal_list'),
    path('approve/', views.journal_approve, name='journal_approve'),
    path('print/<int:pk>/', views.journal_print, name='journal_print'),
    path('details/<int:pk>/', views.journal_details, name='journal_details'),
]