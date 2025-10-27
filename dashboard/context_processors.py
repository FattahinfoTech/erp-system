# dashboard/context_processors.py
from .models import DashboardStats

def dashboard_context(request):
    """
    Context processor to provide dashboard data to all templates
    """
    try:
        stats, created = DashboardStats.objects.get_or_create(pk=1)
        return {
            'dashboard_stats': stats
        }
    except:
        # Return empty context if there's any error
        return {
            'dashboard_stats': None
        }