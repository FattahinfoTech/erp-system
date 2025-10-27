# approve/models.py
from django.db import models

class TransportApprove(models.Model):
    TRANSPORT_CHOICES = [
        ('Transport 1', 'Transport 1'),
        ('Transport 2', 'Transport 2'),
        ('Transport 3', 'Transport 3'),
    ]
    
    WAREHOUSE_CHOICES = [
        ('WH Cox Raw', 'WH Cox Raw'),
        ('WH Cox FG', 'WH Cox FG'),
        ('WH Dhaka Raw', 'WH Dhaka Raw'),
        ('WH Dhaka FG', 'WH Dhaka FG'),
        ('R&D Center, FG', 'R&D Center, FG'),
        ('R&D Center, RAW', 'R&D Center, RAW'),
    ]
    
    invoice_id = models.CharField(max_length=20, unique=True)
    transport = models.CharField(max_length=50, choices=TRANSPORT_CHOICES)
    warehouse = models.CharField(max_length=50, choices=WAREHOUSE_CHOICES)
    address = models.TextField()
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    approved_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_id

    def save(self, *args, **kwargs):
        if not self.invoice_id:
            last_transport = TransportApprove.objects.order_by('-id').first()
            if last_transport:
                last_id = int(last_transport.invoice_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.invoice_id = f"TRANS-{new_id}"
        
        self.total = self.quantity * self.unit_price
        super().save(*args, **kwargs)