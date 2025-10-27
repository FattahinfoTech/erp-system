# dashboard/management/commands/create_initial_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from user_manage.models import UserProfile
from dashboard.models import DashboardStats

class Command(BaseCommand):
    help = 'Create initial data for the ERP system'

    def handle(self, *args, **options):
        # Create default dashboard stats
        DashboardStats.objects.get_or_create(
            pk=1,
            defaults={
                'sales_today': 0,
                'sales_week': 0,
                'sales_month': 0,
                'production_yesterday': 0,
                'production_week': 0,
            }
        )
        
        # Create default admin user if not exists
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@erp.com',
                password='admin123',
                first_name='System',
                last_name='Administrator'
            )
            UserProfile.objects.create(
                user=admin_user,
                employee_id='ADM-001',
                phone='+880XXXXXXXXX',
                address='System Administration',
                role='Admin',
                department='IT'
            )
            self.stdout.write(
                self.style.SUCCESS('Default admin user created: admin/admin123')
            )
        
        self.stdout.write(
            self.style.SUCCESS('Initial data created successfully!')
        )