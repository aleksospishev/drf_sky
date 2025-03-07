from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from materials.models import Course


@shared_task
def send_mail_update_course(course_id):
    course = get_object_or_404(Course, id=course_id)
    subscriptions = course.course_subscription.all()
    recipient_list = [sub.user.email for sub in subscriptions]
    subject = f"обновление {course.name}"
    message = (
        f"Вы подписаны на обновление курса {course.name}, рады вам сообщить что {course.name} обновлен,"
        f" для просмотра пройдите по ссылке http//localhost/materials/{course.id}"
    )

    from_email = settings.EMAIL_HOST_USER
    response = {}

    for recipient in recipient_list:
        try:
            send_mail(subject, message, from_email, [recipient])

            response[recipient] = "Успешно отправлено"
        except Exception as e:
            response = f"{recipient}: Ошибка: {str(e)}"
            response[recipient] = f"Ошибка: {str(e)}"

    print(response)
