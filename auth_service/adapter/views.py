from auth_service.domain import models
from auth_service.domain import commands
from auth_service.adapter import repository


def register_user(cmd: commands.RegisterUser):
    """
    Base level view that handels the flow of user data

    Passing data to the repository for the final validation

    ORM for creating user
    """
    models.user_factory(**cmd.dict())
    repository_ = repository.UserSQLRepository()
    repository_.register_user(**cmd.dict())
