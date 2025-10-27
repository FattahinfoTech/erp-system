# settings_app/models.py
from django.db import models

class ClusterZone(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Pending', 'Pending'),
    ]
    
    cluster = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cluster} - {self.zone}"

class FinishProductType(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Pending', 'Pending'),
    ]
    
    type_title = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type_title

class CustomerCategory(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Pending', 'Pending'),
    ]
    
    category_title = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

class EmailSetting(models.Model):
    TYPE_CHOICES = [
        ('Sale Create', 'Sale Create'),
        ('Sale Audit', 'Sale Audit'),
        ('Sale Approve', 'Sale Approve'),
        ('Sale Cancel', 'Sale Cancel'),
        ('Sale Delivery', 'Sale Delivery'),
        ('Purchase Create', 'Purchase Create'),
        ('Purchase Audit', 'Purchase Audit'),
        ('Purchase Cancel', 'Purchase Cancel'),
        ('Purchase Approve', 'Purchase Approve'),
        ('Purchase Finish Create', 'Purchase Finish Create'),
        ('Purchase Finish Approve', 'Purchase Finish Approve'),
        ('Production Create', 'Production Create'),
        ('Production Qc', 'Production Qc'),
        ('Production Approve', 'Production Approve'),
        ('Production Raw', 'Production Raw'),
        ('Transfer Create', 'Transfer Create'),
        ('Transfer Approve', 'Transfer Approve'),
        ('Transfer Receive', 'Transfer Receive'),
        ('Cash Receive', 'Cash Receive'),
        ('Cash Payment', 'Cash Payment'),
    ]
    
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    emails = models.TextField(help_text="Comma separated email addresses")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type