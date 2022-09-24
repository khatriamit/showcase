from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.models import JobInfo
from cv_service.services.handlers import (
    JobInfoViewSet,
    PersonalInfoViewSet,
    EducationInfoViewSet,
    WorkInfoViewSet,
)

router = DefaultRouter()
router.register("job_info", JobInfoViewSet, basename="job_info")
router.register("personal_info", PersonalInfoViewSet, basename="personal_info")
router.register("education_info", EducationInfoViewSet, basename="education_info")
router.register("work_info", WorkInfoViewSet, basename="work_info")

urlpatterns = [
    path("", include(router.urls)),
]
