# lc_manage/models.py
from django.db import models

class Consignee(models.Model):
    CONSIGNEE_TYPE_CHOICES = [
        ('Local', 'Local'),
        ('Overseas', 'Overseas'),
        ('Both', 'Both'),
    ]
    
    type = models.CharField(max_length=10, choices=CONSIGNEE_TYPE_CHOICES)
    name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    reg_number = models.CharField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class LC(models.Model):
    STATUS_CHOICES = [
        ('Running', 'Running'),
        ('Pending', 'Pending'),
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    
    product_name = models.CharField(max_length=200)
    consignee = models.ForeignKey(Consignee, on_delete=models.CASCADE)
    exporter_info = models.TextField()
    registration_no = models.CharField(max_length=100)
    mother_vessel = models.CharField(max_length=200)
    lc_bank = models.CharField(max_length=200)
    lc_bank_branch = models.CharField(max_length=200)
    exporter_country = models.CharField(max_length=100)
    lc_account = models.CharField(max_length=100)
    lc_number = models.CharField(max_length=100, unique=True)
    allot_lc_number = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    lc_open_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.lc_number