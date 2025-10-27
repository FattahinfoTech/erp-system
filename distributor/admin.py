# distributor/admin.py
from django.contrib import admin
from .models import MPO, ASM, RSM, SM, Area, RouteAssignment

@admin.register(MPO)
class MPOAdmin(admin.ModelAdmin):
    list_display = ['mpo_id', 'name', 'contact', 'status']
    list_filter = ['status']
    search_fields = ['mpo_id', 'name']

@admin.register(ASM)
class ASMAdmin(admin.ModelAdmin):
    list_display = ['asm_id', 'name', 'mobile', 'asm_code', 'zone_name', 'status']
    list_filter = ['status']
    search_fields = ['asm_id', 'name', 'asm_code']

@admin.register(RSM)
class RSMAdmin(admin.ModelAdmin):
    list_display = ['rsm_id', 'name', 'contact', 'rsm_code', 'region_name', 'status']
    list_filter = ['status']
    search_fields = ['rsm_id', 'name', 'rsm_code']

@admin.register(SM)
class SMAdmin(admin.ModelAdmin):
    list_display = ['sm_id', 'name', 'contact', 'sm_code', 'status']
    list_filter = ['status']
    search_fields = ['sm_id', 'name', 'sm_code']

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['route_id', 'route_name', 'tr_code', 'district', 'thana', 'status']
    list_filter = ['district', 'status']
    search_fields = ['route_id', 'route_name', 'district']

@admin.register(RouteAssignment)
class RouteAssignmentAdmin(admin.ModelAdmin):
    list_display = ['assignment_id', 'sm', 'rsm', 'asm', 'mpo', 'route', 'status']
    list_filter = ['status']
    search_fields = ['assignment_id']