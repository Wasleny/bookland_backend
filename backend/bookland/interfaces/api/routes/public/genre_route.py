from fastapi import APIRouter, Depends

from bookland.interfaces.api.schemas import ResponseEnvelopeSchema, GenreResponseSchema
from bookland.interfaces.api.docs import ALL_GENRES_SUCCESS_RESPONSE
from bookland.interfaces.api.services import get_get_all_genres_usecase
from bookland.application.usecases import GetAllGenresUseCase

router = APIRouter()


@router.get(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**ALL_GENRES_SUCCESS_RESPONSE},
)
async def get_genres(usecase: GetAllGenresUseCase = Depends(get_get_all_genres_usecase)):
    genres = await usecase.execute()

    return ResponseEnvelopeSchema(
        message="Gêneros literários encontrados.",
        data={"genres": [GenreResponseSchema.from_entity(genre) for genre in genres]},
    )
