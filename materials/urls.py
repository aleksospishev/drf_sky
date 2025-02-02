from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig

from .views import (CourseViewSet, LessonCreateAPIView, LessonDestroyAPIView,
                    LessonListAPIView, LessonRetrieveAPIView,
                    LessonUpdateAPIView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)
urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons-list"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-detail"),
    path(
        "lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson-update"
    ),
    path(
        "lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson-delete"
    ),
]
urlpatterns += router.urls
