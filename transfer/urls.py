# transfer/urls.py (updated)
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.transfer_create, name='transfer_create'),
    path('approve/', views.transfer_approve, name='transfer_approve'),
    path('receive/', views.transfer_receive, name='transfer_receive'),
    path('approve/<int:transfer_id>/', views.approve_transfer, name='approve_transfer'),
    path('receive/<int:transfer_id>/', views.receive_transfer, name='receive_transfer'),
]