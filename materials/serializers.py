from rest_framework import serializers
from materials.models import Course, Lesson, Subscription
from materials.validators import validate_video_url


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(
        validators=[
            validate_video_url,
        ]
    )

    class Meta:
        model = Lesson
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription  # type: ignore
        fields = ['course']


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    course_lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(source="lesson_set", many=True, read_only=True)
    subscription = serializers.SerializerMethodField()


    def get_course_lesson_count(self, object):
        return object.lesson_set.count()

    def get_subscription(self, object):
        user = self.context.get('request', None).user
        return object.course_subscription.filter(user=user).exists()

    class Meta:
        model = Course
        fields = "__all__"
