from cv_service.domain import models
from cv_service.domain import commands
from cv_service.adapter import repository


def create_jobinfo(cmd: commands.JobInfo):
    models.jobinfo_factory(**cmd.dict())
    repository_ = repository.JobInfoSQLRepository()
    repository_.create_jobinfo(**cmd.dict())


def create_personalinfo(cmd: commands.PersonalInfo):
    models.personalinfo_factory(**cmd.dict())
    repository_ = repository.PersonalInfoSQLRepository()
    repository_.create_personalinfo(**cmd.dict())


def create_educationinfo(cmd: commands.EducationInfo):
    models.educationinfo_factory(**cmd.dict())
    repository_ = repository.EducationInfoSQLRepository()
    repository_.create_educationinfo(**cmd.dict())


def create_workinfo(cmd: commands.WorkInfo):
    models.workinfo_factory(**cmd.dict())
    repository_ = repository.WorkInfoSQLRepository()
    repository_.create_workinfo(**cmd.dict())
