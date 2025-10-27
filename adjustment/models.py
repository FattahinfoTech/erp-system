# adjustment/models.py
from django.db import models

class ProductPlus(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
    ]
    
    adjustment_id = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=200)
    entry_date = models.DateField()
    product = models.CharField(max_length=200)
    godown = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adjustment_id

    def save(self, *args, **kwargs):
        if not self.adjustment_id:
            last_adjustment = ProductPlus.objects.order_by('-id').first()
            if last_adjustment:
                last_id = int(last_adjustment.adjustment_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.adjustment_id = f"ADJ-PLUS-{new_id}"
        super().save(*args, **kwargs)

class ProductMinus(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
    ]
    
    adjustment_id = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=200)
    entry_date = models.DateField()
    product = models.CharField(max_length=200)
    godown = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adjustment_id

    def save(self, *args, **kwargs):
        if not self.adjustment_id:
            last_adjustment = ProductMinus.objects.order_by('-id').first()
            if last_adjustment:
                last_id = int(last_adjustment.adjustment_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.adjustment_id = f"ADJ-MINUS-{new_id}"
        super().save(*args, **kwargs)