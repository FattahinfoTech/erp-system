# reports/models.py
from django.db import models

class ReportLog(models.Model):
    REPORT_TYPE_CHOICES = [
        ('Accounts Report', 'Accounts Report'),
        ('Cash Report', 'Cash Report'),
        ('Sale Report', 'Sale Report'),
        ('Bank Report', 'Bank Report'),
        ('Admin Report', 'Admin Report'),
        ('Warehouse Report', 'Warehouse Report'),
        ('Allotment Report', 'Allotment Report'),
        ('Journal Report', 'Journal Report'),
    ]
    
    report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES)
    generated_by = models.CharField(max_length=100)
    parameters = models.JSONField()  # Store search parameters
    generated_at = models.DateTimeField(auto_now_add=True)
    download_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.report_type} - {self.generated_at}"