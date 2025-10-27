# edit_modify/models.py
from django.db import models

class TransactionEdit(models.Model):
    TRANSACTION_TYPES = [
        ('Sale', 'Sale'),
        ('Purchase', 'Purchase'),
        ('Bank', 'Bank'),
        ('Cash', 'Cash'),
        ('Journal', 'Journal'),
        ('Allotment', 'Allotment'),
    ]
    
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    transaction_id = models.CharField(max_length=100)
    updated_fields = models.JSONField()  # Store which fields were updated
    old_values = models.JSONField()  # Store old values
    new_values = models.JSONField()  # Store new values
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.transaction_id}"