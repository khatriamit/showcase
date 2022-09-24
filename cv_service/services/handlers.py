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
    permission_classes = [IsAuthenticated]
    serializer_class = JobInfoSerializer

    def get_queryset(self):
        queryset = JobInfo.objects.filter(created_by=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.JobInfo(**serializer.validated_data)
        views.create_jobinfo(cmd=cmd, user=self.request.user)

        return Response(
            {"success": "job info created successfully"},
            status=status.HTTP_201_CREATED,
        )


class PersonalInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PersonalInfoSerializer

    def get_queryset(self):
        queryset = PersonalInfo.objects.filter(created_by=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.PersonalInfo(**serializer.validated_data)
        views.create_personalinfo(cmd=cmd, user=self.request.user)

        return Response(
            {"success": "personal info created successfully"},
            status=status.HTTP_201_CREATED,
        )


class EducationInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EducationInfoSerializer

    def get_queryset(self):
        queryset = EducationInfo.objects.filter(created_by=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.EducationInfo(**serializer.validated_data)
        views.create_educationinfo(cmd=cmd, user=self.request.user)

        return Response(
            {"success": "education info created successfully"},
            status=status.HTTP_201_CREATED,
        )


class WorkInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkInfoSerializer

    def get_queryset(self):
        queryset = WorkInfo.objects.filter(created_by=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.WorkInfo(**serializer.validated_data)
        views.create_workinfo(cmd=cmd, user=self.request.user)

        return Response(
            {"success": "work info created successfully"},
            status=status.HTTP_201_CREATED,
        )


class LanguageInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LanguageInfoSerializer

    def get_queryset(self):
        queryset = LanguageInfo.objects.filter(created_by=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.LanguageInfo(**serializer.validated_data)
        views.create_languageinfo(cmd=cmd, user=self.request.user)

        return Response(
            {"success": "Language info created successfully"},
            status=status.HTTP_201_CREATED,
        )


class GetMyCvView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset_ji = JobInfo.objects.filter(created_by=self.request.user).first()
        queryset_pi = PersonalInfo.objects.filter(created_by=self.request.user).first()
        queryset_ei = EducationInfo.objects.filter(created_by=self.request.user).first()
        queryset_wi = WorkInfo.objects.filter(created_by=self.request.user).first()
        queryset_li = LanguageInfo.objects.filter(created_by=self.request.user).first()

        data = {
            "job_info": JobInfoSerializer(queryset_ji).data,
            "personal_info": PersonalInfoSerializer(queryset_pi).data,
            "education_info": EducationInfoSerializer(queryset_ei).data,
            "work_info": WorkInfoSerializer(queryset_wi).data,
            "language_info": LanguageInfoSerializer(queryset_li).data,
        }
        return Response(data)
