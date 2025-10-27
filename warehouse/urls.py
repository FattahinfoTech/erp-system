# warehouse/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('mother-to-lighter/', views.mother_to_lighter, name='mother_to_lighter'),
    path('lighter-to-ghat/', views.lighter_to_ghat, name='lighter_to_ghat'),
    path('ghat-to-dump/', views.ghat_to_dump, name='ghat_to_dump'),
    path('lv-activity/', views.lv_activity, name='lv_activity'),
    path('correction/', views.correction, name='correction'),
    path('do-change/', views.do_change, name='do_change'),
    path('transfer/', views.transfer, name='transfer'),
]