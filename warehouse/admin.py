# warehouse/admin.py
from django.contrib import admin
from .models import MotherToLighter, LighterToGhat, GhatToDump, LVActivity, Correction, DOChange, Transfer

@admin.register(MotherToLighter)
class MotherToLighterAdmin(admin.ModelAdmin):
    list_display = ['lc_number', 'mother_vessel', 'lighter_vessel', 'quantity', 'arrival_date']
    list_filter = ['arrival_date']
    search_fields = ['lc_number', 'mother_vessel']

@admin.register(LighterToGhat)
class LighterToGhatAdmin(admin.ModelAdmin):
    list_display = ['lc_number', 'lighter_vessel', 'received_godown', 'moving_date']
    list_filter = ['moving_date']
    search_fields = ['lc_number', 'lighter_vessel']

@admin.register(GhatToDump)
class GhatToDumpAdmin(admin.ModelAdmin):
    list_display = ['lc_number', 'godown', 'dump', 'update_date']
    list_filter = ['update_date']
    search_fields = ['lc_number', 'godown__name']

@admin.register(LVActivity)
class LVActivityAdmin(admin.ModelAdmin):
    list_display = ['lc_number', 'lighter_vessel', 'mobile_no', 'charpatra_date']
    list_filter = ['charpatra_date']
    search_fields = ['lc_number', 'lighter_vessel']

@admin.register(Correction)
class CorrectionAdmin(admin.ModelAdmin):
    list_display = ['correction_id', 'lc_number', 'mother_vessel', 'edit_quantity']
    search_fields = ['correction_id', 'lc_number']

@admin.register(DOChange)
class DOChangeAdmin(admin.ModelAdmin):
    list_display = ['do_number', 'customer', 'log_center', 'delivery_date']
    list_filter = ['log_center', 'delivery_date']
    search_fields = ['do_number', 'customer']

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['product_info', 'from_godown', 'to_godown', 'quantity', 'transfer_date']
    list_filter = ['transfer_date']
    search_fields = ['product_info', 'lc_number']