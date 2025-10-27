# user_manage/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, UserPermission
from .forms import CustomUserCreationForm, UserProfileForm, UserPermissionForm

@login_required
def user_list(request):
    users = User.objects.all().select_related('userprofile')
    return render(request, 'user_manage/user_list.html', {'users': users})

@login_required
def create_user(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            messages.success(request, 'User created successfully!')
            return redirect('user_list')
    else:
        user_form = CustomUserCreationForm()
        profile_form = UserProfileForm()

    return render(request, 'user_manage/create_user.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            messages.success(request, 'User updated successfully!')
            return redirect('user_list')
    else:
        user_form = CustomUserCreationForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'user_manage/edit_user.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user
    })

@login_required
def set_permissions(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    permissions = UserPermission.objects.filter(user=user)
    
    if request.method == 'POST':
        # Handle permission updates
        for permission in permissions:
            can_view = request.POST.get(f'view_{permission.id}', False)
            can_create = request.POST.get(f'create_{permission.id}', False)
            can_edit = request.POST.get(f'edit_{permission.id}', False)
            can_delete = request.POST.get(f'delete_{permission.id}', False)
            can_approve = request.POST.get(f'approve_{permission.id}', False)
            
            permission.can_view = bool(can_view)
            permission.can_create = bool(can_create)
            permission.can_edit = bool(can_edit)
            permission.can_delete = bool(can_delete)
            permission.can_approve = bool(can_approve)
            permission.save()
        
        messages.success(request, 'Permissions updated successfully!')
        return redirect('user_list')

    # Create default permissions if they don't exist
    modules = [
        'Dashboard', 'Manage', 'LC Manage', 'Purchase', 'Journal', 
        'Accounting', 'Sales', 'Warehouse', 'Allotment', 'Adjustment',
        'Settings', 'Transfer', 'Edit/Modify', 'Receive Transaction',
        'Payment Transaction', 'Petty Cash', 'Reports', 'Approve', 'Distributor'
    ]
    
    for module in modules:
        UserPermission.objects.get_or_create(user=user, module=module)
    
    permissions = UserPermission.objects.filter(user=user)
    
    return render(request, 'user_manage/set_permissions.html', {
        'user': user,
        'permissions': permissions
    })