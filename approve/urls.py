# approve/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('transport/', views.transport_approve, name='transport_approve'),
    path('transport/history/', views.transport_history, name='transport_history'),
    path('transport/approve/<int:pk>/', views.approve_transport, name='approve_transport'),
]