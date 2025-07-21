from fastapi import APIRouter, Depends
from uuid import uuid4

from bookland.interfaces.api.services import (
    get_login_user_usecase,
    get_register_user_usecase,
)
from bookland.interfaces.api.schemas import (
    LoginUserSchema,
    RegisterUserSchema,
    UserSchema,
    AuthResponseSchema,
)
from bookland.interfaces.api.security import (
    create_access_token,
    get_password_hash,
)
from bookland.domain.enums import UserGender, UserRole
from bookland.domain.value_objects import Name, Nickname, Email, Password, BirthDate
from bookland.domain.entities import User
from bookland.interfaces.api.responses import (
    unauthorized_response,
    bad_request_response,
)
from bookland.interfaces.api.docs import (
    USER_BAD_REQUEST,
    USER_UNAUTHORIZED,
)
from bookland.interfaces.api.messages import user_messages

router = APIRouter()


@router.post(
    "/register",
    response_model=AuthResponseSchema,
    responses={**USER_BAD_REQUEST},
)
async def register_user(
    user_data: RegisterUserSchema,
    usecase=Depends(get_register_user_usecase),
):
    """
    Registra um usuário no sistema.
    """
    try:
        Password(user_data.password)
        hashed_password = get_password_hash(user_data.password)

        new_user = User(
            id=str(uuid4()),
            name=Name(user_data.name),
            nickname=Nickname(user_data.nickname),
            email=Email(user_data.email),
            password=Password(hashed_password),
            gender=(
                UserGender(user_data.gender)
                if user_data.gender
                else UserGender.UNSPECIFIED
            ),
            birthdate=BirthDate(user_data.birthdate) if user_data.birthdate else None,
            avatar_url=user_data.avatar_url,
            role=UserRole.USER,
        )

        current_user = await usecase.execute(new_user)
        access_token = create_access_token(data={"sub": current_user.id})
    
        return AuthResponseSchema.from_entity(
            UserSchema.from_entity(current_user),
            access_token,
            user_messages.REGISTER_USER_MESSAGE,
        )
    except Exception as e:
        return bad_request_response(str(e))


@router.post(
    "/login",
    response_model=AuthResponseSchema,
    responses={**USER_UNAUTHORIZED},
)
@router.post("/login")
async def login_user(
    credentials: LoginUserSchema,
    usecase=Depends(get_login_user_usecase),
):
    """
    Autentica um usuário no sistema.
    """
    try:
        user = await usecase.execute(
            Email(credentials.email), Password(credentials.password)
        )

        if not user:
            return unauthorized_response()

        access_token = create_access_token(data={"sub": user.id})

        return AuthResponseSchema.from_entity(
            UserSchema.from_entity(user),
            access_token,
            user_messages.LOGIN_USER_MESSAGE,
        )

    except Exception as e:
        return bad_request_response(str(e))
