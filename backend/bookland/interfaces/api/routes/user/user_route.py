from fastapi import APIRouter, Depends

from bookland.interfaces.api.schemas import UserResponseSchema, UserSchema
from bookland.interfaces.api.docs import (
    USER_SUCCESS_RESPONSE,
    USER_NOT_FOUND_RESPONSE,
    FORBIDDEN_RESPONSE,
)
from bookland.interfaces.api.responses import user_not_found_response
from bookland.interfaces.api.deps import owner_required, get_current_user
from bookland.interfaces.api.services import get_get_user_by_id_usecase
from bookland.interfaces.api.messages import user_messages

router = APIRouter()


@router.get(
    "/{user_id}",
    response_model=UserResponseSchema,
    responses={
        **USER_SUCCESS_RESPONSE,
        **USER_NOT_FOUND_RESPONSE,
        **FORBIDDEN_RESPONSE,
    },
)
async def get_user(
    user_id: str,
    current_user=Depends(get_current_user),
    usecase=Depends(get_get_user_by_id_usecase),
):
    """Recupera os dados do usuário pelo ID."""
    
    await owner_required(user_id, current_user)

    user = await usecase.execute(user_id)

    if not user:
        return user_not_found_response()

    return UserResponseSchema.from_entity(
        UserSchema.from_entity(user),
        user_messages.GET_USER_MESSAGE,
    )
