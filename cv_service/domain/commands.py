from datetime import date
from typing import Optional
from pydantic import BaseModel as Model, validator


class JobInfo(Model):
    job_categories: str
    position: str
    available_for: str
    specializations: Optional[str]
    skills: str
    expected_salary: int
    current_salary: int
    carrer_summery: str


class PersonalInfo(Model):
    mobile: str
    temporary_address: str
    permanent_address: str
    gender: Optional[str]
    dob: date
    marital_status: Optional[bool]
    religion: str


class EducationInfo(Model):
    degree: str
    program: str
    board: str
    institiue_name: Optional[str]
    currently_studying: Optional[bool]
    marks: str
    graduation_year: date


class WorkInfo(Model):
    company_name: str
    type: str
    board: str
    location: str
    job_title: Optional[str]
    level: Optional[str]
    end_date: date
    start_date: date
    responsiblity: str
    is_current: Optional[bool]
