# warehouse/models.py
from django.db import models
from manage_app.models import Godown, Dump
from lc_manage.models import LC

class MotherToLighter(models.Model):
    lc_number = models.CharField(max_length=100)
    mother_vessel = models.CharField(max_length=200)
    lighter_vessel = models.CharField(max_length=200)
    carrying_contractor = models.CharField(max_length=200)
    product_info = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    arrival_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lc_number} - {self.mother_vessel}"

class LighterToGhat(models.Model):
    lc_number = models.CharField(max_length=100)
    lighter_vessel = models.CharField(max_length=200)
    product_info = models.CharField(max_length=200)
    moving_date = models.DateField()
    received_godown = models.ForeignKey(Godown, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lc_number} - {self.lighter_vessel}"

class GhatToDump(models.Model):
    lc_number = models.CharField(max_length=100)
    godown = models.ForeignKey(Godown, on_delete=models.CASCADE)
    lighter_vessel = models.CharField(max_length=200)
    product_info = models.CharField(max_length=200)
    update_date = models.DateField()
    note = models.TextField(blank=True)
    dump = models.ForeignKey(Dump, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lc_number} - {self.godown.name}"

class LVActivity(models.Model):
    lc_number = models.CharField(max_length=100)
    lighter_vessel = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    mv = models.CharField(max_length=200)
    cary_id = models.CharField(max_length=100)
    lighter_freight = models.DecimalField(max_digits=15, decimal_places=2)
    srv_id = models.CharField(max_length=100)
    survey_bill = models.DecimalField(max_digits=15, decimal_places=2)
    load_quan_asper_survey = models.DecimalField(max_digits=15, decimal_places=2)
    actual_received_quantity = models.DecimalField(max_digits=15, decimal_places=2)
    payable_quantity = models.DecimalField(max_digits=15, decimal_places=2)
    time_not_to_count = models.CharField(max_length=100)
    cause = models.TextField()
    short_ex = models.CharField(max_length=100)
    charpatra_date = models.DateField()
    load_start_time = models.DateTimeField()
    load_complete_time = models.DateTimeField()
    sailing_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    discharge_start_time = models.DateTimeField()
    discharge_complete_time = models.DateTimeField()
    sale_center = models.CharField(max_length=200)
    landing_ghat_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lc_number} - {self.lighter_vessel}"

class Correction(models.Model):
    lc_number = models.CharField(max_length=100)
    date = models.DateField()
    correction_id = models.CharField(max_length=100)
    mother_vessel = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    lc_quantity = models.DecimalField(max_digits=15, decimal_places=2)
    edit_quantity = models.DecimalField(max_digits=15, decimal_places=2)
    edit_lc_trader = models.CharField(max_length=200)
    edit_reg_no = models.CharField(max_length=100)
    edit_allot_lc = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.correction_id} - {self.lc_number}"

class DOChange(models.Model):
    LOG_CENTER_CHOICES = [
        ('Admin', 'Admin'),
        ('Noapara', 'Noapara'),
        ('Nagarbari', 'Nagarbari'),
        ('Chittagong', 'Chittagong'),
        ('Narayanganj', 'Narayanganj'),
        ('Ashugang', 'Ashugang'),
        ('Dhaka', 'Dhaka'),
    ]
    
    date = models.DateField()
    log_center = models.CharField(max_length=20, choices=LOG_CENTER_CHOICES)
    do_number = models.CharField(max_length=100)
    customer = models.CharField(max_length=200)
    sale_detail = models.TextField()
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    lc_number = models.CharField(max_length=100)
    dv_from = models.CharField(max_length=200)
    godown = models.CharField(max_length=200)
    gudam = models.CharField(max_length=200)
    delivery_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.do_number} - {self.customer}"

class Transfer(models.Model):
    product_info = models.CharField(max_length=200)
    lc_number = models.CharField(max_length=100)
    from_godown = models.ForeignKey(Godown, on_delete=models.CASCADE, related_name='from_transfers')
    from_dump = models.ForeignKey(Dump, on_delete=models.CASCADE, related_name='from_transfers')
    transfer_date = models.DateField()
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    to_godown = models.ForeignKey(Godown, on_delete=models.CASCADE, related_name='to_transfers')
    to_dump = models.ForeignKey(Dump, on_delete=models.CASCADE, related_name='to_transfers')
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_info} - {self.from_godown} to {self.to_godown}"