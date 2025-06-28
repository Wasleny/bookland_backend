from pydantic import BaseModel, EmailStr, Field
from datetime import date

from bookland.domain.enums.user_role import UserRole
from bookland.domain.enums.user_gender import UserGender


class UserIdSchema(BaseModel):
    user_id: str = Field(..., description="ID do usuário")


class RegisterUserSchema(BaseModel):
    name: str = Field(
        ..., min_length=3, max_length=20, description="Nome completo do usuário"
    )
    nickname: str = Field(
        ..., min_length=3, max_length=30, description="Nickname do usuário"
    )
    email: EmailStr = Field(..., description="Email válido do usuário")
    password: str = Field(
        ..., min_length=8, description="Senha do usuário com pelo menos 8 caracteres"
    )
    gender: UserGender | None = Field(None, description="Gênero do usuário")
    birthday: date | None = Field(None, description="Data de nascimento")
    avatar_url: str | None = Field(None, description="URL do avatar do usuário")
    role: UserRole = Field(..., description="Papel do usuário no sistema")


class LoginUserSchema(BaseModel):
    email: EmailStr = Field(..., description="Email válido do usuário")
    password: str = Field(
        ..., min_length=8, description="Senha do usuário com pelo menos 8 caracteres"
    )


class GetUserSchema(UserIdSchema): ...


class DemoteFromAdminUserSchema(UserIdSchema): ...


class PromoteFromAdminUserSchema(UserIdSchema): ...


class SearchUserSchema(BaseModel):
    email: EmailStr = Field(..., description="Email válido do usuário")


class UserResponseSchema(BaseModel):
    id: str = Field(..., description="ID do usuário")
    name: str = Field(..., description="Nome completo do usuário")
    nickname: str = Field(..., description="Nickname do usuário")
    email: EmailStr = Field(..., description="Email válido do usuário")
    gender: UserGender | None = Field(None, description="Gênero do usuário")
    birthday: date | None = Field(None, description="Data de nascimento")
    avatar_url: str | None = Field(None, description="URL do avatar do usuário")
    role: UserRole = Field(..., description="Papel do usuário no sistema")

    @classmethod
    def from_entity(cls, user):
        return cls(
            id=user.id,
            name=user.name.value,
            nickname=user.nickname.value,
            email=user.email.value,
            gender=user.gender,
            birthday=user.birthday.value,
            avatar_url=user.avatar_url,
            role=user.role,
        )


class AuthDataSchema(BaseModel):
    token: str
    user: UserResponseSchema


class AuthResponseSchema(BaseModel):
    message: str
    data: AuthDataSchema
