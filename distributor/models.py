# distributor/models.py
from django.db import models

class MPO(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    
    mpo_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mpo_id} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.mpo_id:
            last_mpo = MPO.objects.order_by('-id').first()
            if last_mpo:
                last_id = int(last_mpo.mpo_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.mpo_id = f"MPO-{new_id}"
        super().save(*args, **kwargs)

class ASM(models.Model):
    asm_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    asm_code = models.CharField(max_length=50)
    zone_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asm_id} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.asm_id:
            last_asm = ASM.objects.order_by('-id').first()
            if last_asm:
                last_id = int(last_asm.asm_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.asm_id = f"ASM-{new_id}"
        super().save(*args, **kwargs)

class RSM(models.Model):
    rsm_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    rsm_code = models.CharField(max_length=50)
    region_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rsm_id} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.rsm_id:
            last_rsm = RSM.objects.order_by('-id').first()
            if last_rsm:
                last_id = int(last_rsm.rsm_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.rsm_id = f"RSM-{new_id}"
        super().save(*args, **kwargs)

class SM(models.Model):
    sm_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    sm_code = models.CharField(max_length=50)
    status = models.CharField(max_length=10, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sm_id} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.sm_id:
            last_sm = SM.objects.order_by('-id').first()
            if last_sm:
                last_id = int(last_sm.sm_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.sm_id = f"SM-{new_id}"
        super().save(*args, **kwargs)

class Area(models.Model):
    route_id = models.CharField(max_length=20, unique=True)
    route_name = models.CharField(max_length=200)
    tr_code = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    thana = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    location_detail = models.TextField()
    status = models.CharField(max_length=10, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.route_id} - {self.route_name}"

    def save(self, *args, **kwargs):
        if not self.route_id:
            last_area = Area.objects.order_by('-id').first()
            if last_area:
                last_id = int(last_area.route_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.route_id = f"ROUTE-{new_id}"
        super().save(*args, **kwargs)

class RouteAssignment(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    
    assignment_id = models.CharField(max_length=20, unique=True)
    sm = models.ForeignKey(SM, on_delete=models.CASCADE, related_name='assignments')
    rsm = models.ForeignKey(RSM, on_delete=models.CASCADE, related_name='assignments')
    asm = models.ForeignKey(ASM, on_delete=models.CASCADE, related_name='assignments')
    mpo = models.ForeignKey(MPO, on_delete=models.CASCADE, related_name='assignments')
    route = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='assignments')
    depo = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.assignment_id}"

    def save(self, *args, **kwargs):
        if not self.assignment_id:
            last_assignment = RouteAssignment.objects.order_by('-id').first()
            if last_assignment:
                last_id = int(last_assignment.assignment_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 10000001
            self.assignment_id = f"ASSIGN-{new_id}"
        super().save(*args, **kwargs)