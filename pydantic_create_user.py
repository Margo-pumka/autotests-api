from pydantic import BaseModel, EmailStr, Field, UUID4, ConfigDict
from pydantic.alias_generators import to_camel

from clients.users.public_users_client import get_public_users_client
from tools.fakers import get_random_email


class UserSchema(BaseModel):
    """
    Схема структуры пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: UUID4
    email: EmailStr = Field(min_length=1, max_length=250)
    lastName: str = Field(min_length=1, max_length=50)
    firstName: str = Field(min_length=1, max_length=50)
    middleName: str = Field(min_length=1, max_length=50)


class CreateUserRequestSchema(BaseModel):
    """
    Схема структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr = Field(min_length=1, max_length=250, default_factory=lambda: get_random_email())
    password: str = Field(min_length=1, max_length=250, default="string")
    lastName: str = Field(min_length=1, max_length=50, default="string")
    firstName: str = Field(min_length=1, max_length=50, default="string")
    middleName: str = Field(min_length=1, max_length=50, default="string")


class CreateUserResponseSchema(BaseModel):
    """
    Схема структуры ответа создания пользователя.
    """
    user: UserSchema
