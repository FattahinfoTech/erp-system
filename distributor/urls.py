# distributor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('mpo/', views.mpo_list, name='mpo_list'),
    path('asm/', views.asm_list, name='asm_list'),
    path('rsm/', views.rsm_list, name='rsm_list'),
    path('sm/', views.sm_list, name='sm_list'),
    path('area/', views.area_list, name='area_list'),
    path('route/', views.route_list, name='route_list'),
]