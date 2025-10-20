# core/admin.py
from django.contrib import admin
from .models import User, Book, Loan, Reservation, AuditLog
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    fieldsets = DefaultUserAdmin.fieldsets + (
        ("Extra", {"fields": ("role",)}),
    )

admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Reservation)
admin.site.register(AuditLog)
# saritaS