from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


# Create your models here.
class User(AbstractUser):
    Username = None

    email = models.EmailField(
        max_length=25, unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Укажите телефон",
    )
    city = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatar",
        blank=True,
        null=True,
        verbose_name="автар",
        help_text="Ваше фото",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    CHOISES = {"Cash": "Наличные", "Card": "банковский перевод"}
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="user")
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        verbose_name="course",
        related_name="payments_course",
        blank=True,
        null=True,
    )
    lessons = models.ForeignKey(
        Lesson,
        on_delete=models.PROTECT,
        verbose_name="lessons",
        related_name="payments_lesson",
        blank=True,
        null=True,
    )
    payment_amount = models.IntegerField(verbose_name="сумма платежа")
    date_paymate = models.DateField(verbose_name="дата платежа", auto_now=True)
    form_of_paymate = models.CharField(
        choices=CHOISES, default=CHOISES["Cash"], verbose_name="Способ оплаты"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
