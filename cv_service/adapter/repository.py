from app import models as orm
from django.db import transaction


class JobInfoSQLRepository:
    def __init__(self) -> None:
        pass

    def create_jobinfo(
        self,
        job_categories,
        position,
        available_for,
        specializations,
        skills,
        expected_salary,
        current_salary,
        carrer_summery,
        user,
    ):
        """
        ORM query for adding job info

        Params: job_categories, position,available_for,
                specializations,skills,expected_salary,
                current_salary, carrer_summery, user,

        Returns orm object
        """
        with transaction.atomic():
            job_info = orm.JobInfo.objects.create(
                job_categories=job_categories,
                position=position,
                available_for=available_for,
                specializations=specializations,
                skills=skills,
                expected_salary=expected_salary,
                current_salary=current_salary,
                carrer_summery=carrer_summery,
                created_by=user,
            )
            return job_info


class PersonalInfoSQLRepository:
    def __init__(self) -> None:
        pass

    def create_personalinfo(
        self,
        mobile,
        temporary_address,
        permanent_address,
        gender,
        dob,
        marital_status,
        religion,
        user,
    ):
        """
        ORM query for adding personal info

        Params: mobile, temporary_address, permanent_address,
                gender,dob,marital_status,religion, user,

        Returns orm object
        """
        with transaction.atomic():
            personal_info = orm.PersonalInfo.objects.create(
                mobile=mobile,
                temporary_address=temporary_address,
                permanent_address=permanent_address,
                gender=gender,
                dob=dob,
                marital_status=marital_status,
                religion=religion,
                created_by=user,
            )
            return personal_info


class EducationInfoSQLRepository:
    def __init__(self) -> None:
        pass

    def create_educationinfo(
        self,
        degree,
        program,
        board,
        institiue_name,
        currently_studying,
        marks,
        graduation_year,
        user,
    ):
        """
        ORM query for adding education info

        Params: degree,program,board,institiue_name,
                currently_studying,marks,graduation_year,
                user,

        Returns orm object
        """
        with transaction.atomic():
            education_info = orm.EducationInfo.objects.create(
                degree=degree,
                program=program,
                board=board,
                institiue_name=institiue_name,
                currently_studying=currently_studying,
                marks=marks,
                graduation_year=graduation_year,
                created_by=user,
            )
            return education_info


class WorkInfoSQLRepository:
    def __init__(self) -> None:
        pass

    def create_workinfo(
        self,
        company_name,
        type,
        board,
        location,
        job_title,
        level,
        start_date,
        end_date,
        responsiblity,
        is_current,
        user,
    ):
        """
        ORM query for adding work info

        Params: degree,program,board,institiue_name,
                currently_studying,marks,graduation_year,
                user,

        Returns orm object
        """
        with transaction.atomic():
            work_info = orm.WorkInfo.objects.create(
                company_name=company_name,
                type=type,
                board=board,
                location=location,
                job_title=job_title,
                level=level,
                start_date=start_date,
                end_date=end_date,
                responsiblity=responsiblity,
                is_current=is_current,
                created_by=user,
            )
            return work_info


class LanguageInfoSQLRepository:
    def __init__(self) -> None:
        pass

    def create_languageinfo(
        self,
        language,
        speaking,
        reading,
        writing,
        listening,
        user,
    ):
        """
        ORM query for adding language info

        Params: language,speaking,reading,writing,
                listening, user,

        Returns orm object
        """
        with transaction.atomic():
            language_info = orm.LanguageInfo.objects.create(
                language=language,
                speaking=speaking,
                reading=reading,
                writing=writing,
                listening=listening,
                created_by=user,
            )
            return language_info
