# receive_transaction/models.py
from django.db import models

class CashReceive(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
    ]
    
    receive_id = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=200)
    receive_amount = models.DecimalField(max_digits=15, decimal_places=2)
    receive_note = models.TextField()
    description = models.TextField()
    voucher_number = models.CharField(max_length=100)
    entry_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.receive_id

    def save(self, *args, **kwargs):
        if not self.receive_id:
            last_receive = CashReceive.objects.order_by('-id').first()
            if last_receive:
                last_id = int(last_receive.receive_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.receive_id = f"CR-{new_id}"
        super().save(*args, **kwargs)

class BankReceive(models.Model):
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
    
    receive_id = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=200)
    receive_bank_name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    note = models.TextField()
    description = models.TextField()
    entry_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.receive_id

    def save(self, *args, **kwargs):
        if not self.receive_id:
            last_receive = BankReceive.objects.order_by('-id').first()
            if last_receive:
                last_id = int(last_receive.receive_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.receive_id = f"BR-{new_id}"
        super().save(*args, **kwargs)

class DealerBankReceive(models.Model):
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
    
    receive_id = models.CharField(max_length=20, unique=True)
    district = models.CharField(max_length=100)
    thana = models.CharField(max_length=100)
    dealer = models.CharField(max_length=200)
    receive_bank_name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    note = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.receive_id

    def save(self, *args, **kwargs):
        if not self.receive_id:
            last_receive = DealerBankReceive.objects.order_by('-id').first()
            if last_receive:
                last_id = int(last_receive.receive_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.receive_id = f"DBR-{new_id}"
        super().save(*args, **kwargs)