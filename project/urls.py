from django.contrib import admin
from django.urls import path

# from blog_service.entrypoint.routes import urlpatterns as blog_url
from cv_service.entrypoint.routes import urlpatterns as cv_url
from auth_service.entrypoint.routes import urlpatterns as auth_url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

# urlpatterns += blog_url
urlpatterns += cv_url
urlpatterns += auth_url
