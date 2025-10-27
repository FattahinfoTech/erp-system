# journal/models.py
from django.db import models

class Journal(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Posted', 'Posted'),
    ]
    
    journal_id = models.CharField(max_length=20, unique=True)
    date = models.DateField()
    voucher_number = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.journal_id

    def save(self, *args, **kwargs):
        if not self.journal_id:
            last_journal = Journal.objects.order_by('-id').first()
            if last_journal:
                last_id = int(last_journal.journal_id)
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.journal_id = str(new_id)
        super().save(*args, **kwargs)

class JournalEntry(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='entries')
    trn_id = models.CharField(max_length=50)
    account_debit = models.CharField(max_length=200)
    account_credit = models.CharField(max_length=200)
    lc_number = models.CharField(max_length=100, blank=True)
    note = models.TextField(blank=True)
    debit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.journal.journal_id} - {self.trn_id}"