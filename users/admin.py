# Register your models here.
from django.contrib import admin

from .models import Payments, User


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    """Модель администрирования пользователей."""

    list_display = (
        "email",
        "avatar",
        "city",
        "phone",
        "is_active",
    )
    list_filter = ("email",)
    search_fields = ("email", "phone")


@admin.register(Payments)
class Paymentadmin(admin.ModelAdmin):
    pass
