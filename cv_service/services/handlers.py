from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from app.models import (
    EducationInfo,
    JobInfo,
    LanguageInfo,
    PersonalInfo,
    User,
    WorkInfo,
)
from cv_service.services.serializer import (
    EducationInfoSerializer,
    JobInfoSerializer,
    LanguageInfoSerializer,
    PersonalInfoSerializer,
    WorkInfoSerializer,
)
from cv_service.domain import commands
from cv_service.adapter import views


class JobInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = JobInfoSerializer

    def get_queryset(self):
        queryset = JobInfo.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.JobInfo(**serializer.validated_data)
        views.create_jobinfo(cmd=cmd)

        return Response(
            {"success": "job info created successfully"},
            status=status.HTTP_201_CREATED,
        )


class PersonalInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PersonalInfoSerializer

    def get_queryset(self):
        queryset = PersonalInfo.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.PersonalInfo(**serializer.validated_data)
        views.create_personalinfo(cmd=cmd)

        return Response(
            {"success": "personal info created successfully"},
            status=status.HTTP_201_CREATED,
        )


class EducationInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = EducationInfoSerializer

    def get_queryset(self):
        queryset = EducationInfo.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.EducationInfo(**serializer.validated_data)
        views.create_educationinfo(cmd=cmd)

        return Response(
            {"success": "education info created successfully"},
            status=status.HTTP_201_CREATED,
        )


class WorkInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = WorkInfoSerializer

    def get_queryset(self):
        queryset = WorkInfo.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.WorkInfo(**serializer.validated_data)
        views.create_workinfo(cmd=cmd)

        return Response(
            {"success": "work info created successfully"},
            status=status.HTTP_201_CREATED,
        )


class LanguageInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = LanguageInfoSerializer

    def get_queryset(self):
        queryset = LanguageInfo.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.LanguageInfo(**serializer.validated_data)
        views.create_languageinfo(cmd=cmd)

        return Response(
            {"success": "Language info created successfully"},
            status=status.HTTP_201_CREATED,
        )
