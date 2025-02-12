from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from users.models import User


@shared_task
def disactive_user():
    users = User.objects.filter(last_login__lt=now() - timedelta(minutes=60))
    if users.count() > 0:
        users.update(is_active=False)
        users.save()
