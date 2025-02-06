from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from rest_framework import views

from materials.models import Course, Lesson, Subscription
from materials.pagination import CustomPaginator
from materials.serializers import (
    CourseDetailSerializer,
    CourseSerializer,
    LessonSerializer,
SubscriptionSerializer
)
from users.permissions import IsModer, IsOwner


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CustomPaginator


    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [~IsModer]
        elif self.action in ("list", "retrieve", "update", "partial_update"):
            permission_classes = [IsModer | IsOwner]
        else:# self.action == "destroy":
            permission_classes = [~IsModer | IsOwner]
        return [permission() for permission in permission_classes]


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [~IsModer]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModer | IsOwner]


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModer | IsOwner]
    pagination_class = CustomPaginator


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModer | IsOwner]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]


class CourseSubscribeApiView(views.APIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    # permission_classes = [??]

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')

        course_item = get_object_or_404(Course, id=course_id)

        sub_item = self.queryset.filter(user=user, course=course_item)

        if sub_item.exists():
            sub_item.delete()
            message = 'подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'
            # Возвращаем ответ в API
        return Response({"message": message})