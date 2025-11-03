# accounts/models.py (часть A)
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserA(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def full_name(self):
        parts = [self.first_name, self.middle_name, self.last_name]
        return " ".join(p for p in parts if p)
