# user_manage/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.create_user, name='create_user'),
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('permissions/<int:user_id>/', views.set_permissions, name='set_permissions'),
]