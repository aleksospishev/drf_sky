from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User

from .models import Course, Lesson, Subscription


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="test@example_test.test")
        self.course = Course.objects.create(name="test", owner=self.user)
        self.lesson = Lesson.objects.create(
            name="test_lesson",
            course=self.course,
            video_url="https://yotube.com/1123/",
            owner=self.user,
        )
        self.course_sub = Subscription.objects.create(
            user=self.user, course=self.course
        )
        self.client.force_authenticate(user=self.user)

    def test_list_lesson(self):
        url = reverse("materials:lessons-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "video_url": "https://yotube.com/1123/",
                    "name": "test_lesson",
                    "preview": None,
                    "descriptions": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson-detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        # print(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("materials:lesson-create")
        data = {
            "name": "test_lesson_2",
            "course": self.course.pk,
            "video_url": "https://youtube.com/1234/",
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)
        print(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        data = {"name": "test-lesson-2"}
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "test-lesson-2")

    def test_lesson_delete(self):
        url = reverse("materials:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class CourseSubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@example_test.test",
        )
        self.course = Course.objects.create(name="test_course", owner=self.user)
        self.lesson = Lesson.objects.create(
            name="test-course_lesson",
            course=self.course,
            video_url="https://www.youtube.com/3532",
            owner=self.user,
        )
        self.course_subscription = Subscription(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_course_subscribe(self):
        url = reverse("materials:subscribe", args=(self.course.pk,))
        data = {"course": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["message"], "подписка добавлена")

        data = {"course": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["message"], "подписка удалена")
