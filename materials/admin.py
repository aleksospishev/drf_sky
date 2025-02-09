# Register your models here.
from django.contrib import admin

from .models import Course, Lesson


@admin.register(Lesson)
class Lessonadmin(admin.ModelAdmin):
    """Модель администрирования пользователей."""

    list_display = ("name", "preview", "video_url")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Course)
class Courseadmin(admin.ModelAdmin):
    list_display = ("name", "descriptions")
    list_filter = ("name", "descriptions")
    search_fields = ("name",)
