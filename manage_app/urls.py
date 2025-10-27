# manage_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('godowns/', views.godown_list, name='godown_list'),
    path('dumps/', views.dump_list, name='dump_list'),
    path('cost-centers/', views.cost_center_list, name='cost_center_list'),
]