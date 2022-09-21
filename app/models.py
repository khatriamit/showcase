from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from app.constants import GENDER, JOB_POSITIONS, LANGUAGES, ORGANIZATION_TYPE, RELIGION

User = get_user_model()


class CommonInfo(models.Model):
    """
    common info that is frequently to be used in every model
    """

    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, db_index=True
    )
    created_on = models.DateTimeField("Created at", auto_now_add=True, db_index=True)
    created_by = models.ForeignKey(
        User,
        verbose_name="Created by",
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_created",
        on_delete=models.SET_NULL,
    )
    modified_on = models.DateTimeField("Last modified at", auto_now=True, db_index=True)
    modified_by = models.ForeignKey(
        User,
        verbose_name="Modified by",
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_modified",
        on_delete=models.SET_NULL,
    )

    class Meta:
        abstract = True


class Blog(CommonInfo):
    title = models.CharField(max_length=150)
    heading = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["created_on"]
        db_table = "blog"
        verbose_name = "Blog"
        verbose_name_plural = "Blog"


class JobInfo(CommonInfo):
    job_categories = models.CharField(max_length=250)
    position = models.CharField(max_length=20, choices=JOB_POSITIONS)
    available_for = models.CharField(max_length=30)
    specializations = models.CharField(max_length=250, null=True, blank=True)
    skills = models.TextField()
    expected_salary = models.PositiveIntegerField()
    current_salary = models.PositiveIntegerField()
    carrer_summery = models.TextField()

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        ordering = ["created_on"]
        db_table = "job_info"
        verbose_name = "JobInfo"
        verbose_name_plural = "JobsInfo"


class PersonalInfo(CommonInfo):
    mobile = models.CharField(max_length=20)
    temporary_address = models.CharField(max_length=150)
    permanent_address = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=GENDER)
    dob = models.DateField()
    marital_status = models.BooleanField(default=False)
    religion = models.CharField(max_length=10, choices=RELIGION)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        ordering = ["created_on"]
        db_table = "personal_info"
        verbose_name = "PersonalInfo"
        verbose_name_plural = "PersonalInfo"


class EducationInfo(CommonInfo):
    degree = models.CharField(max_length=150)
    program = models.CharField(max_length=150)
    board = models.CharField(max_length=150)
    institiue_name = models.CharField(max_length=150)
    currently_studying = models.BooleanField(default=False)
    marks = models.CharField(max_length=20)
    graduation_year = models.DateField()

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        ordering = ["created_on"]
        db_table = "education_info"
        verbose_name = "EducationInfo"
        verbose_name_plural = "EducationsInfo"


class WorkInfo(CommonInfo):
    company_name = models.CharField(max_length=150)
    type = models.CharField(max_length=50, choices=ORGANIZATION_TYPE)
    board = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150)
    level = models.CharField(max_length=20, choices=JOB_POSITIONS)
    start_date = models.DateField()
    end_date = models.DateField()
    responsiblity = models.TextField()
    is_current = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        ordering = ["created_on"]
        db_table = "work_info"
        verbose_name = "WorkInfo"
        verbose_name_plural = "WorksInfo"


class LanguageInfo(CommonInfo):
    language = models.CharField(max_length=50, choices=LANGUAGES)
    speaking = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ],
    )
    reading = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ],
    )
    writing = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ],
    )
    listening = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ],
    )

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        ordering = ["created_on"]
        db_table = "language_info"
        verbose_name = "LanguageInfo"
        verbose_name_plural = "LanguagesInfo"
