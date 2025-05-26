from rest_framework.serializers import ValidationError


def validate_video_url(value):
    if "youtube.com" not in value:
        raise ValidationError(
            "Этот сайт не поддерживается. Загрузите контент с видеохостинга YouTube.com."
        )
