# purchase/models.py
from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    district = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    purchase_id = models.CharField(max_length=20, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purchase_id

    def save(self, *args, **kwargs):
        if not self.purchase_id:
            last_purchase = Purchase.objects.order_by('-id').first()
            if last_purchase:
                last_id = int(last_purchase.purchase_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.purchase_id = f"PUR-{new_id}"
        super().save(*args, **kwargs)