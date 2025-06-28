from fastapi import APIRouter, status
from uuid import uuid4

from bookland.interfaces.api.schemas.user import (
    LoginUserSchema,
    RegisterUserSchema,
    UserResponseSchema,
    AuthResponseSchema,
    AuthDataSchema,
)
from bookland.infra.repositories.mongo_repositories.mongo_user_repository import (
    MongoUserRepository,
)
from bookland.application.usecases.user.login_user import LoginUserUseCase
from bookland.application.usecases.user.register_user import RegisterUserUseCase
from bookland.interfaces.api.security import (
    create_access_token,
    get_password_hash,
)
from bookland.domain.value_objects.name_vo import Name
from bookland.domain.value_objects.nickname_vo import Nickname
from bookland.domain.value_objects.email_vo import Email
from bookland.domain.value_objects.password_vo import Password
from bookland.domain.value_objects.birthday_vo import Birthday
from bookland.domain.entities.user import User
from bookland.interfaces.api.responses.user.user_error_responses import (
    unauthorized_response,
    bad_request_response,
)
from bookland.interfaces.api.docs.user_response_docs import (
    USER_BAD_REQUEST,
    USER_UNAUTHORIZED,
)

router = APIRouter()
repository = MongoUserRepository()


@router.post(
    "/register",
    response_model=AuthResponseSchema,
    responses={**USER_BAD_REQUEST},
)
async def register_user(user_data: RegisterUserSchema):
    usecase = RegisterUserUseCase(repository)

    hashed_password = get_password_hash(user_data.password)

    new_user = User(
        id=str(uuid4()),
        name=Name(user_data.name),
        nickname=Nickname(user_data.nickname),
        email=Email(user_data.email),
        password=Password(hashed_password),
        gender=user_data.gender,
        birthday=Birthday(user_data.birthday) if user_data.birthday else None,
        avatar_url=user_data.avatar_url,
        role=user_data.role,
    )

    try:
        current_user = await usecase.execute(new_user)

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
    usecase = LoginUserUseCase(repository)

    user = await usecase.execute(credentials.email, credentials.password)

    if not user:
        return unauthorized_response()

    access_token = create_access_token(data={"sub": user.id})

    return AuthResponseSchema(
        message="Login realizado com sucesso.",
        data=AuthDataSchema(
            token=access_token, user=UserResponseSchema.from_entity(user)
        ),
    )
