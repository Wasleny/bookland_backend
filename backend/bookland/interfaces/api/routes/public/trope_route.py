from fastapi import APIRouter, Depends

from bookland.interfaces.api.schemas import ResponseEnvelopeSchema, TropeResponseSchema
from bookland.interfaces.api.docs import TROPES_SUCCESS_RESPONSE
from bookland.interfaces.api.services import get_all_tropes_usecase

router = APIRouter()


@router.get(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**TROPES_SUCCESS_RESPONSE},
)
async def get_tropes():
    tropes = await get_all_tropes_usecase.execute()

    return ResponseEnvelopeSchema(
        message="Tropes literárias encontradas.",
        data={"tropes": [TropeResponseSchema.from_entity(trope) for trope in tropes]},
    )
