from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите навание курса",
                        max_length=25,
                        unique=True,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Превью курса",
                        null=True,
                        upload_to="materials/course",
                        verbose_name="Заставка",
                    ),
                ),
                (
                    "price",
                    models.PositiveIntegerField(default=100, verbose_name="Цена"),
                ),
                (
                    "descriptions",
                    models.TextField(
                        blank=True, help_text="Введите описание курса.", null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
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
            ],
            options={
                "verbose_name": "Оплата за курс",
                "verbose_name_plural": "Оплата за курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите навание урока",
                        max_length=25,
                        unique=True,
                        verbose_name="Название урока",
                    ),
                ),
                (
                    "descriptions",
                    models.TextField(
                        blank=True, help_text="Введите описание урока.", null=True
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Превью курса",
                        null=True,
                        upload_to="materials/lesson",
                        verbose_name="Заставка",
                    ),
                ),
                ("video_url", models.URLField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
        migrations.CreateModel(
            name="Subscription",
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
            ],
            options={
                "verbose_name": "Подсписка на курс.",
                "verbose_name_plural": "Подписки на курсы.",
            },
        ),
    ]
