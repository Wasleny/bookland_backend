from fastapi import APIRouter, Depends

from bookland.interfaces.api.schemas import (
    UserResponseSchema,
    DemoteFromAdminUserSchema,
    PromoteFromAdminUserSchema,
    SearchUserSchema,
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
    search_user_usecase,
)


router = APIRouter(
    dependencies=[Depends(admin_required)],
    responses={**USER_UNAUTHORIZED, **FORBIDDEN_RESPONSE},
)


@router.patch(
    "/demote-admin",
    response_model=ResponseEnvelopeSchema,
    responses={**USER_SUCCESS_RESPONSE, **USER_NOT_FOUND_RESPONSE},
)
async def demote_from_admin(user_data: DemoteFromAdminUserSchema):
    user = await get_user_by_id_usecase.execute(user_data.user_id)

    if not user:
        return user_not_found_response()

    updated_user = await demote_user_from_admin_usecase.execute(user)

    return ResponseEnvelopeSchema(
        message="Usuário rebaixado para usuário comum com sucesso.",
        data={"user": UserResponseSchema.from_entity(updated_user)},
    )


@router.patch(
    "/promote-admin",
    response_model=ResponseEnvelopeSchema,
    responses={**USER_SUCCESS_RESPONSE, **USER_NOT_FOUND_RESPONSE},
)
async def promote_to_admin(user_data: PromoteFromAdminUserSchema):
    user = await get_user_by_id_usecase.execute(user_data.user_id)

    if not user:
        return user_not_found_response()

    updated_user = await promote_user_to_admin_usecase.execute(user)

    return ResponseEnvelopeSchema(
        message="Usuário promovido para administrador com sucesso.",
        data={"user": UserResponseSchema.from_entity(updated_user)},
    )


@router.post(
    "/search",
    response_model=ResponseEnvelopeSchema,
    responses={**USER_SEARCH_RESPONSES},
)
async def search_user(user_data: SearchUserSchema):
    user = await search_user_usecase.execute(user_data.email)

    if not user:
        return empty_search_result_response()

    return ResponseEnvelopeSchema(
        message="Usuário encontrado com sucesso.",
        data={"user": UserResponseSchema.from_entity(user)},
    )
