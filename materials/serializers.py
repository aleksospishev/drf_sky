from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    course_lesson_count = SerializerMethodField()
    lesson = LessonSerializer(source="lesson_set", many=True)

    def get_course_lesson_count(self, object):
        return object.lesson_set.count()

    class Meta:
        model = Course
        fields = "__all__"
