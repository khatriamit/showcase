from django.db import transaction
from rest_framework import serializers
from app.models import (
    EducationInfo,
    LanguageInfo,
    PersonalInfo,
    User,
    JobInfo,
    WorkInfo,
)


class JobInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobInfo
        fields = [
            "job_categories",
            "position",
            "available_for",
            "specializations",
            "skills",
            "expected_salary",
            "current_salary",
            "carrer_summery",
        ]


class PersonalInfoSerializer(serializers.ModelSerializer):
    marital_status = serializers.BooleanField(required=True)

    class Meta:
        model = PersonalInfo
        fields = [
            "mobile",
            "temporary_address",
            "permanent_address",
            "gender",
            "dob",
            "marital_status",
            "religion",
        ]


class EducationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationInfo
        fields = [
            "degree",
            "program",
            "board",
            "institiue_name",
            "currently_studying",
            "marks",
            "graduation_year",
        ]


class WorkInfoSerializer(serializers.ModelSerializer):
    is_current = serializers.BooleanField(required=True)

    class Meta:
        model = WorkInfo
        fields = [
            "company_name",
            "type",
            "board",
            "location",
            "job_title",
            "level",
            "start_date",
            "end_date",
            "responsiblity",
            "is_current",
        ]


class LanguageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageInfo
        fields = [
            "language",
            "speaking",
            "reading",
            "writing",
            "listening",
        ]
