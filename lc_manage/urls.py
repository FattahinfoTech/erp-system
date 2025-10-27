# lc_manage/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('consignees/', views.consignee_list, name='consignee_list'),
    path('lcs/', views.lc_list, name='lc_list'),
    path('lcs/update/<int:pk>/', views.update_lc, name='update_lc'),
]