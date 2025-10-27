# sales/models.py
from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    district = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    credit_limit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    status = models.CharField(max_length=10, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.customer_id:
            last_customer = Customer.objects.order_by('-id').first()
            if last_customer:
                last_id = int(last_customer.customer_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.customer_id = f"CUST-{new_id}"
        super().save(*args, **kwargs)

class Sale(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    
    invoice_id = models.CharField(max_length=20, unique=True)
    sale_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    physical_invoice_number = models.CharField(max_length=100)
    truck_number = models.CharField(max_length=50)
    reference_no = models.CharField(max_length=100, blank=True)
    driver_name = models.CharField(max_length=100)
    driver_contact = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_id

    def save(self, *args, **kwargs):
        if not self.invoice_id:
            last_sale = Sale.objects.order_by('-id').first()
            if last_sale:
                last_id = int(last_sale.invoice_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.invoice_id = f"INV-{new_id}"
        super().save(*args, **kwargs)