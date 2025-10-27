# user_manage/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, UserPermission

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'

class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]

class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ['user', 'module', 'can_view', 'can_create', 'can_edit', 'can_delete', 'can_approve']
    list_filter = ['module', 'user']
    search_fields = ['user__username', 'module']

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserPermission, UserPermissionAdmin)