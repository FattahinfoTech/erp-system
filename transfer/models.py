# transfer/models.py
from django.db import models

class TransferManage(models.Model):
    FROM_TO_CHOICES = [
        ('WH Cox Raw', 'WH Cox Raw'),
        ('WH Cox FG', 'WH Cox FG'),
        ('WH Dhaka Raw', 'WH Dhaka Raw'),
        ('WH Dhaka FG', 'WH Dhaka FG'),
        ('R&D Center, FG', 'R&D Center, FG'),
        ('R&D Center, RAW', 'R&D Center, RAW'),
    ]
    
    PRODUCT_TYPE_CHOICES = [
        ('Finish', 'Finish'),
        ('Raw', 'Raw'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Received', 'Received'),
    ]
    
    transfer_id = models.CharField(max_length=20, unique=True)
    date = models.DateField()
    from_location = models.CharField(max_length=20, choices=FROM_TO_CHOICES)
    to_location = models.CharField(max_length=20, choices=FROM_TO_CHOICES)
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transfer_id

    def save(self, *args, **kwargs):
        if not self.transfer_id:
            last_transfer = TransferManage.objects.order_by('-id').first()
            if last_transfer:
                last_id = int(last_transfer.transfer_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.transfer_id = f"TRF-{new_id}"
        super().save(*args, **kwargs)