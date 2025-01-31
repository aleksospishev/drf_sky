from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True,
        verbose_name="Название курса",
        help_text="Введите навание курса",
    )
    preview = models.ImageField(
        upload_to="materials/course",
        blank=True,
        null=True,
        verbose_name="Заставка",
        help_text="Превью курса",
    )
    descriptions = models.TextField(
        null=True, blank=True, help_text="Введите описание курса."
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True,
        verbose_name="Название урока",
        help_text="Введите навание урока",
    )
    descriptions = models.TextField(
        null=True, blank=True, help_text="Введите описание урока."
    )
    preview = models.ImageField(
        upload_to="materials/lesson",
        blank=True,
        null=True,
        verbose_name="Заставка",
        help_text="Превью курса",
    )
    video_url = models.URLField(
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name="lesson_set"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
