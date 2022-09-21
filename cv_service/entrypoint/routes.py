from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile_service.services.handlers import ProfileView

router = DefaultRouter()
router.register("profile", ProfileView, basename="profile")

urlpatterns = [
    path("", include(router.urls)),
]
