# dashboard/admin.py
from django.contrib import admin
from .models import DashboardStats

@admin.register(DashboardStats)
class DashboardStatsAdmin(admin.ModelAdmin):
    list_display = ['sales_today', 'sales_week', 'sales_month', 'production_yesterday', 'production_week', 'updated_at']
    readonly_fields = ['updated_at']