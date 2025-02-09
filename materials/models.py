from django.conf import settings
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
    price = models.PositiveIntegerField(default=100, verbose_name="Цена")

    descriptions = models.TextField(
        null=True, blank=True, help_text="Введите описание курса."
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Автор курса",
        help_text="Укажите автора урока ",
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
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="lessons")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Автор урока",
        help_text="Укажите атора урока",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_subscription",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_subscription",
        verbose_name="Курс",
    )

    class Meta:
        verbose_name = "Подсписка на курс."
        verbose_name_plural = "Подписки на курсы."


class CoursePayment(models.Model):
    """Модель для оплаты курсов"""

    amount = models.PositiveIntegerField(verbose_name="сумма оплаты")
    session_id = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="id сессии"
    )
    link = models.URLField(
        max_length=400, blank=True, null=True, verbose_name="ссылка на оплату"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="user_payments",
        verbose_name="пользователь",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_payment",
        verbose_name="Курс",
    )

    def __str__(self):
        return self.amount

    class Meta:
        verbose_name = "Оплата за курс"
        verbose_name_plural = "Оплата за курсы"
