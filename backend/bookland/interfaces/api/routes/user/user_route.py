from fastapi import APIRouter, Depends

from bookland.infra.repositories.mongo_repositories.mongo_user_repository import (
    MongoUserRepository,
)
from bookland.interfaces.api.schemas.response_envelope import ResponseEnvelopeSchema
from bookland.interfaces.api.docs.user_response_docs import (
    USER_SUCCESS_RESPONSE,
    USER_NOT_FOUND_RESPONSE,
)
from bookland.interfaces.api.schemas.user import GetUserSchema, UserResponseSchema
from bookland.application.usecases.user.get_user_by_id import GetUserByIdUseCase
from bookland.interfaces.api.responses.user.user_error_responses import (
    user_not_found_response,
)
from bookland.interfaces.api.deps import owner_required, get_current_user

router = APIRouter()
repository = MongoUserRepository()


@router.get(
    "/{user_id}",
    response_model=ResponseEnvelopeSchema,
    responses={**USER_SUCCESS_RESPONSE, **USER_NOT_FOUND_RESPONSE},
)
async def get_user(user_id: str, current_user=Depends(get_current_user)):
    await owner_required(user_id, current_user)

    usecase = GetUserByIdUseCase(repository)
    user = await usecase.execute(user_id)

    if not user:
        return user_not_found_response()

    return ResponseEnvelopeSchema(
        message="Usuário encontrado.",
        data={"user": UserResponseSchema.from_entity(user)},
    )
