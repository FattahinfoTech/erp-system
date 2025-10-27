# dashboard/models.py
from django.db import models
from django.contrib.auth.models import User

class DashboardStats(models.Model):
    sales_today = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    sales_week = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    sales_month = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    production_yesterday = models.IntegerField(default=0)
    production_week = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Dashboard Statistics"