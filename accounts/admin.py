from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserA

@admin.register(CustomUserA)
class CustomUserAAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {'fields': ('middle_name', 'date_of_birth')}),
    )
