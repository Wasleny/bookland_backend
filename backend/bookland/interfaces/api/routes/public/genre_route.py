from fastapi import APIRouter, Depends

from bookland.interfaces.api.schemas import ResponseEnvelopeSchema, GenreResponseSchema
from bookland.interfaces.api.docs import GENRES_SUCCESS_RESPONSE
from bookland.interfaces.api.services import get_all_genres_usecase

router = APIRouter()


@router.get(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**GENRES_SUCCESS_RESPONSE},
)
async def get_genres():
    genres = await get_all_genres_usecase.execute()

    return ResponseEnvelopeSchema(
        message="Gêneros literários encontrados.",
        data={"genres": [GenreResponseSchema.from_entity(genre) for genre in genres]},
    )
