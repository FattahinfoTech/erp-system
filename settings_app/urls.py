# settings_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cluster-zone/', views.cluster_zone, name='cluster_zone'),
    path('finish-product-type/', views.finish_product_type, name='finish_product_type'),
    path('customer-category/', views.customer_category, name='customer_category'),
    path('email-setting/', views.email_setting, name='email_setting'),
]