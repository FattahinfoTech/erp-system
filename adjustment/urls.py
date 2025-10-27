# adjustment/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('product-plus/', views.product_plus, name='product_plus'),
    path('product-plus-approve/', views.product_plus_approve, name='product_plus_approve'),
    path('product-minus/', views.product_minus, name='product_minus'),
    path('product-minus-approve/', views.product_minus_approve, name='product_minus_approve'),
]