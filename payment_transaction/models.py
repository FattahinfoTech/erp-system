# payment_transaction/models.py
from django.db import models

class CashPayment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Audited', 'Audited'),
        ('Confirmed', 'Confirmed'),
    ]
    
    payment_id = models.CharField(max_length=20, unique=True)
    account_payment_to = models.CharField(max_length=200)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_note = models.TextField()
    description = models.TextField()
    voucher_number = models.CharField(max_length=100)
    entry_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id

    def save(self, *args, **kwargs):
        if not self.payment_id:
            last_payment = CashPayment.objects.order_by('-id').first()
            if last_payment:
                last_id = int(last_payment.payment_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.payment_id = f"CP-{new_id}"
        super().save(*args, **kwargs)

class BankPayment(models.Model):
    TYPE_CHOICES = [
        ('TT', 'TT'),
        ('BFTN(Queue)', 'BFTN(Queue)'),
        ('Cheque(Queue)', 'Cheque(Queue)'),
        ('NPBS(Instant)', 'NPBS(Instant)'),
        ('RTGS(Instant)', 'RTGS(Instant)'),
        ('Advice', 'Advice'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
    ]
    
    payment_id = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=200)
    payment_bank_name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    note = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id

    def save(self, *args, **kwargs):
        if not self.payment_id:
            last_payment = BankPayment.objects.order_by('-id').first()
            if last_payment:
                last_id = int(last_payment.payment_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.payment_id = f"BP-{new_id}"
        super().save(*args, **kwargs)