from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Создаёт суперпользователя admin, если его нет."

    def handle(self, *args, **options):
        username = "admin"
        email = "admin@example.com"
        password = "admin123"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"✅ Admin created: {username}/{password}"))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Admin already exists"))
