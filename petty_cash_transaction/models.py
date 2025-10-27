# petty_cash_transaction/models.py
from django.db import models

class PettyCash(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('Debit', 'Debit'),
        ('Credit', 'Credit'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Audited', 'Audited'),
        ('Confirmed', 'Confirmed'),
    ]
    
    petty_cash_id = models.CharField(max_length=20, unique=True)
    account = models.CharField(max_length=200)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    note = models.TextField()
    description = models.TextField()
    voucher_number = models.CharField(max_length=100)
    lc_number = models.CharField(max_length=100)
    entry_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.petty_cash_id

    def save(self, *args, **kwargs):
        if not self.petty_cash_id:
            last_petty = PettyCash.objects.order_by('-id').first()
            if last_petty:
                last_id = int(last_petty.petty_cash_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.petty_cash_id = f"PC-{new_id}"
        super().save(*args, **kwargs)