# allotment/models.py
from django.db import models

class Dealer(models.Model):
    name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    thana = models.CharField(max_length=100)
    dealer_registration = models.CharField(max_length=100)
    dealer_contact = models.CharField(max_length=20)
    dealer_address = models.TextField()
    status = models.CharField(max_length=10, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AllotmentSale(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
    ]
    
    DELIVERY_FROM_CHOICES = [
        ('Mother Vessel', 'Mother Vessel'),
        ('Lighter Vessel', 'Lighter Vessel'),
        ('Godown', 'Godown'),
    ]
    
    STATUS_TYPE_CHOICES = [
        ('Material', 'Material'),
        ('Paper', 'Paper'),
    ]
    
    allotment_id = models.CharField(max_length=20, unique=True)
    district = models.CharField(max_length=100)
    thana = models.CharField(max_length=100)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    lc_number = models.CharField(max_length=100)
    product_info = models.CharField(max_length=200)
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    agri_ir = models.CharField(max_length=100)
    agri_ir_date = models.DateField()
    balance_qty_in_bag = models.DecimalField(max_digits=15, decimal_places=2)
    sale_qty_in_bag = models.DecimalField(max_digits=15, decimal_places=2)
    m_ton = models.DecimalField(max_digits=15, decimal_places=2)
    quantity_in_m_ton = models.DecimalField(max_digits=15, decimal_places=2)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    delivery_product = models.CharField(max_length=200)
    delivery_from = models.CharField(max_length=20, choices=DELIVERY_FROM_CHOICES)
    godown = models.CharField(max_length=200)
    status_type = models.CharField(max_length=10, choices=STATUS_TYPE_CHOICES)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.allotment_id

    def save(self, *args, **kwargs):
        if not self.allotment_id:
            last_allotment = AllotmentSale.objects.order_by('-id').first()
            if last_allotment:
                last_id = int(last_allotment.allotment_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.allotment_id = f"ALLOT-{new_id}"
        super().save(*args, **kwargs)