from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random
from accounts.models import CustomUser
from datetime import datetime

fake=Faker()

DEPARTMENTS = ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
ROLES = ['admin', 'editor', 'viewer']

class Command(BaseCommand):
    help = "Generate 10000 users"
    
    def handle(self, *args, **kwargs):
        total=10000
        batch_size=1000
        password="12345"
        
        for batch_start in range(0, total, batch_size):
            users=[]
            for _ in range(batch_size):
                first_name=fake.first_name()
                last_name=fake.last_name()
                email=fake.unique.email()
                role=random.choice(ROLES)
                
                user=CustomUser(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    is_active=True,
                    is_staff=(role=='admin'),
                    date_joined=timezone.now(),
                )
                user.set_password(password)
                users.append(user)
            
            CustomUser.objects.bulk_create(users)
            self.stdout.write(self.style.SUCCESS(f"Created {min(batch_start + batch_size, total)} / {total} users"))