# manage_app/models.py
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Fertilizer', 'Fertilizer'),
        ('Food Grains', 'Food Grains'),
        ('Cement', 'Cement'),
        ('Mineral', 'Mineral'),
        ('Other', 'Other'),
    ]
    
    UNIT_CHOICES = [
        ('KG', 'KG'),
        ('Bag', 'Bag'),
    ]
    
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Pending', 'Pending'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    product_group = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    title_bengali = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    unit_type = models.CharField(max_length=10, choices=UNIT_CHOICES)
    unit_strength = models.DecimalField(max_digits=10, decimal_places=2)
    open_sale_price = models.DecimalField(max_digits=15, decimal_places=2)
    allotment_sale_price = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Godown(models.Model):
    TYPE_CHOICES = [
        ('Self', 'Self'),
        ('Other', 'Other'),
    ]
    
    SALES_HUB_CHOICES = [
        ('Admin', 'Admin'),
        ('Nowapara', 'Nowapara'),
        ('Nagarbari', 'Nagarbari'),
        ('Chittagong', 'Chittagong'),
        ('Narayanganj', 'Narayanganj'),
        ('Ashugang', 'Ashugang'),
        ('Dhaka', 'Dhaka'),
    ]
    
    name = models.CharField(max_length=200)
    ghat = models.CharField(max_length=200)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    sales_hub = models.CharField(max_length=20, choices=SALES_HUB_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Dump(models.Model):
    godown = models.ForeignKey(Godown, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.godown.name} - {self.name}"

class CostCenter(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Pending', 'Pending'),
    ]
    
    name = models.CharField(max_length=200)
    entry_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name