from fastapi import APIRouter, Depends

from bookland.infra.repositories.mongo_repositories.mongo_user_repository import (
    MongoUserRepository,
)
from bookland.application.usecases.user.demote_user_from_admin import (
    DemoteUserFromAdminUseCase,
)
from bookland.application.usecases.user.promote_user_to_admin import (
    PromoteUserToAdminUseCase,
)
from bookland.application.usecases.user.search_user import SearchUserUseCase
from bookland.interfaces.api.schemas.user import (
    UserResponseSchema,
    DemoteFromAdminUserSchema,
    PromoteFromAdminUserSchema,
    SearchUserSchema,
)
from bookland.interfaces.api.deps import admin_required
from bookland.interfaces.api.responses.user.user_error_responses import (
    user_not_found_response,
)
from bookland.interfaces.api.responses.success_responses import (
    empty_search_result_response,
)
from bookland.interfaces.api.schemas.response_envelope import ResponseEnvelopeSchema
from bookland.interfaces.api.docs.user_response_docs import (
    USER_SUCCESS_RESPONSE,
    USER_NOT_FOUND_RESPONSE,
    USER_SEARCH_RESPONSES,
)


router = APIRouter(dependencies=[Depends(admin_required)])
repository = MongoUserRepository()


@router.patch(
    "/demote-admin",
    response_model=ResponseEnvelopeSchema,
    responses={**USER_SUCCESS_RESPONSE, **USER_NOT_FOUND_RESPONSE},
)
async def demote_from_admin(user_data: DemoteFromAdminUserSchema):
    usecase = DemoteUserFromAdminUseCase(repository)
    user = await repository.get_by_id(user_data.user_id)

    if not user:
        return user_not_found_response()

    updated_user = await usecase.execute(user)

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
    usecase = PromoteUserToAdminUseCase(repository)
    user = await repository.get_by_id(user_data.user_id)

    if not user:
        return user_not_found_response()

    updated_user = await usecase.execute(user)

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
    usecase = SearchUserUseCase(repository)
    user = await usecase.execute(user_data.email)

    if not user:
        return empty_search_result_response()

    return ResponseEnvelopeSchema(
        message="Usuário encontrado com sucesso.",
        data={"user": UserResponseSchema.from_entity(user)},
    )
