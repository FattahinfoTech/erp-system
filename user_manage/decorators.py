# user_manage/decorators.py
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from functools import wraps

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            
            # Check if user has the required role
            if hasattr(request.user, 'userprofile'):
                user_role = request.user.userprofile.role
                if user_role in allowed_roles:
                    return view_func(request, *args, **kwargs)
            
            raise PermissionDenied("You don't have permission to access this page.")
        return _wrapped_view
    return decorator

def permission_required(permission):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            
            # Check custom permissions
            if request.user.userprofile.userpermission_set.filter(
                module=permission, can_view=True
            ).exists():
                return view_func(request, *args, **kwargs)
            
            raise PermissionDenied("You don't have permission to access this page.")
        return _wrapped_view
    return decorator