from fastapi import APIRouter, Depends

from bookland.interfaces.api.schemas import ResponseEnvelopeSchema, UserResponseSchema
from bookland.interfaces.api.docs import (
    USER_SUCCESS_RESPONSE,
    USER_NOT_FOUND_RESPONSE,
    FORBIDDEN_RESPONSE,
)
from bookland.interfaces.api.responses import user_not_found_response
from bookland.interfaces.api.deps import owner_required, get_current_user
from bookland.interfaces.api.services import get_user_by_id_usecase

router = APIRouter()


@router.get(
    "/{user_id}",
    response_model=ResponseEnvelopeSchema,
    responses={
        **USER_SUCCESS_RESPONSE,
        **USER_NOT_FOUND_RESPONSE,
        **FORBIDDEN_RESPONSE,
    },
)
async def get_user(user_id: str, current_user=Depends(get_current_user)):
    await owner_required(user_id, current_user)

    user = await get_user_by_id_usecase.execute(user_id)

    if not user:
        return user_not_found_response()

    return ResponseEnvelopeSchema(
        message="Usuário encontrado.",
        data={"user": UserResponseSchema.from_entity(user)},
    )
