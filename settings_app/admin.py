# settings_app/admin.py
from django.contrib import admin
from .models import ClusterZone, FinishProductType, CustomerCategory, EmailSetting

@admin.register(ClusterZone)
class ClusterZoneAdmin(admin.ModelAdmin):
    list_display = ['cluster', 'zone', 'status']
    list_filter = ['status']
    search_fields = ['cluster', 'zone']

@admin.register(FinishProductType)
class FinishProductTypeAdmin(admin.ModelAdmin):
    list_display = ['type_title', 'value', 'status']
    list_filter = ['status']
    search_fields = ['type_title']

@admin.register(CustomerCategory)
class CustomerCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'status']
    list_filter = ['status']
    search_fields = ['category_title']

@admin.register(EmailSetting)
class EmailSettingAdmin(admin.ModelAdmin):
    list_display = ['type', 'status']
    list_filter = ['type', 'status']
    search_fields = ['type', 'emails']