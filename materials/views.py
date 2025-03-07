from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, CoursePayment, Lesson, Subscription
from materials.pagination import CustomPaginator
from materials.serializers import (CourseDetailSerializer,
                                   CoursePaymentSerializer, CourseSerializer,
                                   LessonSerializer, SubscriptionSerializer)
from materials.services import create_price, create_stripe_session
from materials.tasks import send_mail_update_course
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

    def perform_update(self, serializer):
        course_id = self.kwargs.get("pk")
        send_mail_update_course.delay(course_id)
        serializer.save()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [~IsModer]
        elif self.action in ("list", "retrieve", "update", "partial_update"):
            permission_classes = [IsModer | IsOwner]
        else:
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

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")

        course_item = get_object_or_404(Course, id=course_id)

        sub_item = self.queryset.filter(user=user, course=course_item)

        if sub_item.exists():
            sub_item.delete()
            message = "подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "подписка добавлена"
        return Response({"message": message})


class CoursePaymentCreateApiView(CreateAPIView):
    serializer_class = CoursePaymentSerializer
    queryset = CoursePayment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        course_id = self.request.data.get("course")
        course = get_object_or_404(Course, id=course_id)
        amount_usd = course.price
        payment = serializer.save(amount=amount_usd)
        price = create_price(amount_usd, course.name)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()
