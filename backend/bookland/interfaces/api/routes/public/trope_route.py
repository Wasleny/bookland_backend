from fastapi import APIRouter, Depends

from bookland.interfaces.api.schemas import ResponseEnvelopeSchema, TropeResponseSchema
from bookland.interfaces.api.docs import ALL_TROPES_SUCCESS_RESPONSE
from bookland.interfaces.api.services import get_get_all_tropes_usecase
from bookland.application.usecases import GetAllTropesUseCase

router = APIRouter()


@router.get(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**ALL_TROPES_SUCCESS_RESPONSE},
)
async def get_tropes(
    usecase: GetAllTropesUseCase = Depends(get_get_all_tropes_usecase),
):
    tropes = await usecase.execute()

    return ResponseEnvelopeSchema(
        message="Tropes literárias encontradas.",
        data={"tropes": [TropeResponseSchema.from_entity(trope) for trope in tropes]},
    )
