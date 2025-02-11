# Generated by Django 5.1.5 on 2025-02-09 15:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0007_alter_lesson_course"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CoursePayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField(verbose_name="сумма оплаты")),
                (
                    "session_id",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="id сессии"
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        blank=True,
                        max_length=400,
                        null=True,
                        verbose_name="ссылка на оплату",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_payment",
                        to="materials.course",
                        verbose_name="Курс",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_payments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Оплата за курс",
                "verbose_name_plural": "Оплата за курсы",
            },
        ),
    ]
