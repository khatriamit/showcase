from cv_service.domain import models
from cv_service.domain import commands
from cv_service.adapter import repository


def create_jobinfo(cmd: commands.JobInfo, user):
    models.jobinfo_factory(**cmd.dict())
    repository_ = repository.JobInfoSQLRepository()
    repository_.create_jobinfo(user=user, **cmd.dict())


def create_personalinfo(cmd: commands.PersonalInfo, user):
    models.personalinfo_factory(**cmd.dict())
    repository_ = repository.PersonalInfoSQLRepository()
    repository_.create_personalinfo(user=user, **cmd.dict())


def create_educationinfo(cmd: commands.EducationInfo, user):
    models.educationinfo_factory(**cmd.dict())
    repository_ = repository.EducationInfoSQLRepository()
    repository_.create_educationinfo(user=user, **cmd.dict())


def create_workinfo(cmd: commands.WorkInfo, user):
    models.workinfo_factory(**cmd.dict())
    repository_ = repository.WorkInfoSQLRepository()
    repository_.create_workinfo(user=user, **cmd.dict())


def create_languageinfo(cmd: commands.LanguageInfo, user):
    models.languageinfo_factory(**cmd.dict())
    repository_ = repository.LanguageInfoSQLRepository()
    repository_.create_languageinfo(user=user, **cmd.dict())
