from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import Response, JSONResponse

from bookland.interfaces.api.schemas import (
    UserSchema,
    UserResponseSchema,
    AllUsersResponseSchema,
)
from bookland.interfaces.api.deps import admin_required
from bookland.interfaces.api.responses import (
    user_not_found_response,
    empty_search_result_response,
)
from bookland.interfaces.api.docs import (
    USER_SUCCESS_RESPONSE,
    USER_NOT_FOUND_RESPONSE,
    USER_SEARCH_RESPONSES,
    USER_UNAUTHORIZED,
    FORBIDDEN_RESPONSE,
)
from bookland.interfaces.api.services import (
    get_get_user_by_id_usecase,
    get_demote_user_from_admin_usecase,
    get_promote_user_to_admin_usecase,
    get_get_user_by_email_usecase,
    get_get_users_by_role_usecase,
)
from bookland.interfaces.api.exceptions import forbidden_exception
from bookland.settings import ADMIN_EMAIL
from bookland.interfaces.api.messages import user_messages
from bookland.domain.exceptions import UserNotFoundException

router = APIRouter(
    dependencies=[Depends(admin_required)],
    responses={**USER_UNAUTHORIZED, **FORBIDDEN_RESPONSE},
)


@router.patch(
    "/demote-admin/{id}",
    response_model=UserResponseSchema,
    responses={**USER_SUCCESS_RESPONSE, **USER_NOT_FOUND_RESPONSE},
)
async def demote_from_admin(
    id: str,
    get_user=Depends(get_get_user_by_id_usecase),
    usecase=Depends(get_demote_user_from_admin_usecase),
) -> Response:
    """
    Rebaixa o usuário informado de administrador para usuário comum.
    """
    user = await get_user.execute(id)

    if not user:
        return user_not_found_response()

    if user.email.value == ADMIN_EMAIL:
        raise forbidden_exception(user_messages.SUPER_ADMIN_MESSAGE)

    updated_user = await usecase.execute(user.id)

    return UserResponseSchema.from_entity(
        UserSchema.from_entity(updated_user),
        user_messages.DEMOTE_USER_MESSAGE,
    )


@router.patch(
    "/promote-admin/{id}",
    response_model=UserResponseSchema,
    responses={**USER_SUCCESS_RESPONSE, **USER_NOT_FOUND_RESPONSE},
)
async def promote_to_admin(
    id: str,
    get_user=Depends(get_get_user_by_id_usecase),
    usecase=Depends(get_promote_user_to_admin_usecase),
) -> Response:
    """
    Promove o usuário informado de usuário comum para administrador.
    """
    try:
        updated_user = await usecase.execute(id)

        return UserResponseSchema.from_entity(
            UserSchema.from_entity(updated_user),
            user_messages.PROMOTE_USER_MESSAGE,
        )
    except UserNotFoundException:
        return user_not_found_response()


@router.get(
    "/get-by-email",
    response_model=UserResponseSchema,
    responses={**USER_SEARCH_RESPONSES},
)
async def get_user_by_email(
    email: str = Query(..., description="E-mail do usuário a ser buscado"),
    usecase=Depends(get_get_user_by_email_usecase),
) -> Response:
    """
    Busca usuário pelo e-mail.
    """
    user = await usecase.execute(email)

    if not user:
        return empty_search_result_response()

    return UserResponseSchema.from_entity(
        UserSchema.from_entity(user),
        user_messages.GET_USER_MESSAGE,
    )


@router.get(
    "/get-by-role",
    response_model=AllUsersResponseSchema,
    responses={**USER_SEARCH_RESPONSES},
)
async def get_user_by_role(
    role: str = Query(..., description="Role (papel) dos usuários a serem buscados"),
    usecase=Depends(get_get_users_by_role_usecase),
) -> Response:
    """
    Busca usuários pelo role (papel).
    """
    users = await usecase.execute(role)

    if len(users) == 0:
        return empty_search_result_response()

    return AllUsersResponseSchema.from_entity(
        [UserSchema.from_entity(user) for user in users],
        user_messages.GET_USERS_MESSAGE,
    )
