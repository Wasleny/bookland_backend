from fastapi import APIRouter, Depends, Query
from fastapi.responses import Response, JSONResponse

from bookland.interfaces.api.schemas import (
    UserResponseSchema,
    DemoteFromAdminUserSchema,
    PromoteToAdminUserSchema,
    ResponseEnvelopeSchema,
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
    get_user_by_id_usecase,
    demote_user_from_admin_usecase,
    promote_user_to_admin_usecase,
    get_user_by_email_usecase,
)
from bookland.interfaces.api.exceptions import forbidden_exception
from bookland.settings import ADMIN_EMAIL
from bookland.interfaces.api.messages import user_messages

router = APIRouter(
    dependencies=[Depends(admin_required)],
    responses={**USER_UNAUTHORIZED, **FORBIDDEN_RESPONSE},
)


@router.patch(
    "/demote-admin",
    response_model=ResponseEnvelopeSchema,
    responses={**USER_SUCCESS_RESPONSE, **USER_NOT_FOUND_RESPONSE},
)
async def demote_from_admin(
    user_data: DemoteFromAdminUserSchema,
) -> Response:
    """
    Rebaixa o usuário informado de administrador para usuário comum.
    """
    user = await get_user_by_id_usecase.execute(user_data.user_id)

    if not user:
        return user_not_found_response()

    if user.email.value == ADMIN_EMAIL:
        raise forbidden_exception(user_messages.SUPER_ADMIN_MESSAGE)

    updated_user = await demote_user_from_admin_usecase.execute(user)

    return JSONResponse(
        status_code=200,
        content=ResponseEnvelopeSchema[dict](
            message=user_messages.DEMOTE_USER_MESSAGE,
            data={"user": UserResponseSchema.from_entity(updated_user)},
        ).model_dump(),
    )


@router.patch(
    "/promote-admin",
    response_model=ResponseEnvelopeSchema,
    responses={**USER_SUCCESS_RESPONSE, **USER_NOT_FOUND_RESPONSE},
)
async def promote_to_admin(
    user_data: PromoteToAdminUserSchema,
) -> Response:
    """
    Promove o usuário informado de usuário comum para administrador.
    """
    user = await get_user_by_id_usecase.execute(user_data.user_id)

    if not user:
        return user_not_found_response()

    updated_user = await promote_user_to_admin_usecase.execute(user)

    return JSONResponse(
        status_code=200,
        content=ResponseEnvelopeSchema[dict](
            message=user_messages.PROMOTE_USER_MESSAGE,
            data={"user": UserResponseSchema.from_entity(updated_user)},
        ).model_dump(),
    )


@router.get(
    "/get-by-email",
    response_model=ResponseEnvelopeSchema,
    responses={**USER_SEARCH_RESPONSES},
)
async def get_user_by_email(
    email: str = Query(..., description="E-mail do usuário a ser buscado"),
) -> Response:
    """
    Busca usuário pelo e-mail.
    """
    user = await get_user_by_email_usecase.execute(email)

    if not user:
        return empty_search_result_response()

    return JSONResponse(
        status_code=200,
        content=ResponseEnvelopeSchema[dict](
            message=user_messages.GET_USER_BY_EMAIL_MESSAGE,
            data={"user": UserResponseSchema.from_entity(user)},
        ).model_dump(),
    )
