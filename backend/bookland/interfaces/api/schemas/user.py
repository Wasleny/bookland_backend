from pydantic import BaseModel, EmailStr, Field
from datetime import date

from bookland.domain.enums import UserRole, UserGender


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
    birthdate: date | None = Field(None, description="Data de nascimento")
    avatar_url: str | None = Field(None, description="URL do avatar do usuário")


class LoginUserSchema(BaseModel):
    email: EmailStr = Field(..., description="Email válido do usuário")
    password: str = Field(
        ..., min_length=8, description="Senha do usuário com pelo menos 8 caracteres"
    )


class UserSchema(BaseModel):
    id: str = Field(..., description="ID do usuário")
    name: str = Field(..., description="Nome completo do usuário")
    nickname: str = Field(..., description="Nickname do usuário")
    email: EmailStr = Field(..., description="Email válido do usuário")
    gender: UserGender | None = Field(None, description="Gênero do usuário")
    age: int | None = Field(None, description="Idade do usuário")
    birthdate: str | None = Field(None, description="Data de nascimento")
    ratings_count: int = Field(..., description="Número de avaliações do usuário")
    reviews_count: int = Field(..., description="Número de resenhas do usuário")
    average_rating: float = Field(..., description="Média de avaliações do usuário")
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
            age=user.birthdate.age() if user.birthdate else None,
            birthdate=user.birthdate.to_json() if user.birthdate else None,
            ratings_count=user.ratings_count,
            reviews_count=user.reviews_count,
            average_rating=(
                user.average_rating.value
                if user.average_rating.value is not None
                else 0.0
            ),
            avatar_url=user.avatar_url,
            role=user.role,
        )


class AuthResponseSchema(BaseModel):
    token: str = Field(..., description="Token de acesso do usuário")
    message: str = Field(..., description="Mensagem")
    user: UserSchema = Field(..., description="Dados do usuário autenticado")

    @classmethod
    def from_entity(cls, user, access_token, message):
        return cls(
            token=access_token,
            message=message,
            user=user,
        )


class UserResponseSchema(BaseModel):
    message: str = Field(..., description="Mensagem")
    user: UserSchema = Field(..., description="Dados do usuário")

    @classmethod
    def from_entity(cls, user, message):
        return cls(
            message=message,
            user=user,
        )


class AllUsersResponseSchema(BaseModel):
    message: str = Field(..., description="Mensagem")
    users: list[UserSchema] = Field(..., description="Lista de usuários")

    @classmethod
    def from_entity(cls, users, message):
        return cls(
            message=message,
            users=users,
        )
