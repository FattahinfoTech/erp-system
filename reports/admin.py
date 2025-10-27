# reports/admin.py
from django.contrib import admin
from .models import ReportLog

@admin.register(ReportLog)
class ReportLogAdmin(admin.ModelAdmin):
    list_display = ['report_type', 'generated_by', 'generated_at', 'download_count']
    list_filter = ['report_type', 'generated_at']
    search_fields = ['report_type', 'generated_by']
    readonly_fields = ['generated_at']