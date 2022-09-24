from datetime import date
import typing
from pydantic import BaseModel


class JobInfo(BaseModel):
    job_categories: str
    position: str
    available_for: str
    specializations: typing.Optional[str]
    skills: str
    expected_salary: int
    current_salary: int
    carrer_summery: str

    class Config:
        arbitrary_types_allowed = True

    def update(self, **mapping: typing.Dict):
        return self.copy(update=mapping)


def jobinfo_factory(
    job_categories: str,
    position: str,
    available_for: str,
    specializations: typing.Optional[str],
    skills: str,
    expected_salary: int,
    current_salary: int,
    carrer_summery: str,
) -> JobInfo:
    return PersonalInfo(
        job_categories=job_categories,
        position=position,
        available_for=available_for,
        specializations=specializations,
        skills=skills,
        expected_salary=expected_salary,
        current_salary=current_salary,
        carrer_summery=carrer_summery,
    )


class PersonalInfo(BaseModel):
    mobile: str
    temporary_address: str
    permanent_address: str
    gender: typing.Optional[str]
    dob: date
    marital_status: typing.Optional[bool]
    religion: str

    class Config:
        arbitrary_types_allowed = True

    def update(self, **mapping: typing.Dict):
        return self.copy(update=mapping)


def personalinfo_factory(
    mobile: str,
    temporary_address: str,
    permanent_address: str,
    gender: typing.Optional[str],
    dob: date,
    marital_status: typing.Optional[bool],
    religion: str,
) -> PersonalInfo:
    return PersonalInfo(
        mobile=mobile,
        temporary_address=temporary_address,
        permanent_address=permanent_address,
        gender=gender,
        dob=dob,
        marital_status=marital_status,
        religion=religion,
    )


class EducationInfo(BaseModel):
    degree: str
    program: str
    board: str
    institiue_name: typing.Optional[str]
    currently_studying: typing.Optional[bool]
    marks: str
    graduation_year: date

    class Config:
        arbitrary_types_allowed = True

    def update(self, **mapping: typing.Dict):
        return self.copy(update=mapping)


def educationinfo_factory(
    degree: str,
    program: str,
    board: str,
    institiue_name: typing.Optional[str],
    currently_studying: typing.Optional[bool],
    marks: str,
    graduation_year: date,
) -> EducationInfo:
    return EducationInfo(
        degree=degree,
        program=program,
        board=board,
        institiue_name=institiue_name,
        currently_studying=currently_studying,
        marks=marks,
        graduation_year=graduation_year,
    )


class WorkInfo(BaseModel):
    company_name: str
    type: str
    board: str
    job_title: typing.Optional[str]
    level: typing.Optional[str]
    end_date: date
    start_date: date
    responsiblity: str
    is_current: typing.Optional[bool]

    class Config:
        arbitrary_types_allowed = True

    def update(self, **mapping: typing.Dict):
        return self.copy(update=mapping)


def workinfo_factory(
    company_name: str,
    type: str,
    board: str,
    location: str,
    job_title: typing.Optional[str],
    level: typing.Optional[str],
    end_date: date,
    start_date: date,
    responsiblity: str,
    is_current: typing.Optional[bool],
) -> WorkInfo:
    return WorkInfo(
        company_name=company_name,
        type=type,
        board=board,
        job_title=job_title,
        location=location,
        level=level,
        end_date=end_date,
        start_date=start_date,
        responsiblity=responsiblity,
        is_current=is_current,
    )


class LanguageInfo(BaseModel):
    language: str
    speaking: typing.Optional[int]
    reading: typing.Optional[int]
    writing: typing.Optional[int]
    listening: typing.Optional[int]

    class Config:
        arbitrary_types_allowed = True

    def update(self, **mapping: typing.Dict):
        return self.copy(update=mapping)


def languageinfo_factory(
    language: str,
    speaking: typing.Optional[int],
    reading: typing.Optional[int],
    writing: typing.Optional[int],
    listening: typing.Optional[int],
) -> LanguageInfo:
    return LanguageInfo(
        language=language,
        speaking=speaking,
        reading=reading,
        writing=writing,
        listening=listening,
    )
