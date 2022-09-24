import typing
from pydantic import BaseModel


class User(BaseModel):
    """
    Create a new model by parsing and validating input data from keyword arguments.
    Expects first_name, last_name, usersname, email, password as a class constants .
    """

    first_name: str
    last_name: str
    username: str
    email: str
    password: str

    class Config:
        """
        Added attributes for the model class
        """

        arbitrary_types_allowed = True

    def update(self, **mapping: typing.Dict):
        """
        Handels the updating of the domain model
        """
        return self.copy(update=mapping)


def user_factory(
    first_name: str,
    last_name: str,
    username: str,
    email: str,
    password: str,
) -> User:
    """
    Factory receives the parameters for the domain and reurns the domain model
    """
    return User(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=password,
    )
