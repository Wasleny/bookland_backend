from fastapi import APIRouter
from uuid import uuid4

from bookland.interfaces.api.services import login_user_usecase, register_user_usecase
from bookland.interfaces.api.schemas import (
    LoginUserSchema,
    RegisterUserSchema,
    UserResponseSchema,
    AuthResponseSchema,
    AuthDataSchema,
)
from bookland.interfaces.api.security import (
    create_access_token,
    get_password_hash,
)
from bookland.domain.enums import UserGender, UserRole
from bookland.domain.value_objects import Name, Nickname, Email, Password, Birthday
from bookland.domain.entities.user import User
from bookland.interfaces.api.responses import (
    unauthorized_response,
    bad_request_response,
)
from bookland.interfaces.api.docs import (
    USER_BAD_REQUEST,
    USER_UNAUTHORIZED,
)

router = APIRouter()


@router.post(
    "/register",
    response_model=AuthResponseSchema,
    responses={**USER_BAD_REQUEST},
)
async def register_user(user_data: RegisterUserSchema):
    try:
        Password(user_data.password)
        hashed_password = get_password_hash(user_data.password)

        new_user = User(
            id=str(uuid4()),
            name=Name(user_data.name),
            nickname=Nickname(user_data.nickname),
            email=Email(user_data.email),
            password=Password(hashed_password),
            gender=user_data.gender if user_data.gender else UserGender.UNSPECIFIED,
            birthday=Birthday(user_data.birthday) if user_data.birthday else None,
            avatar_url=user_data.avatar_url,
            role=UserRole.USER,
        )

        current_user = await register_user_usecase.execute(new_user)

        access_token = create_access_token(data={"sub": current_user.id})

        return AuthResponseSchema(
            message="Cadastro realizado com sucesso.",
            data=AuthDataSchema(
                token=access_token, user=UserResponseSchema.from_entity(current_user)
            ),
        )
    except Exception as e:
        return bad_request_response(str(e))


@router.post(
    "/login",
    response_model=AuthResponseSchema,
    responses={**USER_UNAUTHORIZED},
)
@router.post("/login", response_model=AuthResponseSchema)
async def login_user(credentials: LoginUserSchema):
    try:
        user = await login_user_usecase.execute(
            Email(credentials.email), Password(credentials.password)
        )

        if not user:
            return unauthorized_response()

        access_token = create_access_token(data={"sub": user.id})

        return AuthResponseSchema(
            message="Login realizado com sucesso.",
            data=AuthDataSchema(
                token=access_token, user=UserResponseSchema.from_entity(user)
            ),
        )
    except Exception as e:
        return bad_request_response(str(e))
