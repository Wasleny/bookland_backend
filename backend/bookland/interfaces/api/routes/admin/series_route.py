from fastapi import APIRouter, Depends
from uuid import uuid4

from bookland.domain.entities import Series
from bookland.domain.value_objects import Title, Slug
from bookland.interfaces.api.services import (
    create_series_usecase,
    get_all_series_usecase,
    get_series_usecase,
    update_series_usecase,
    soft_delete_series_usecase,
)
from bookland.interfaces.api.schemas import (
    CreateSeriesSchema,
    UpdateSeriesSchema,
    SeriesResponseSchema,
    ResponseEnvelopeSchema,
)
from bookland.interfaces.api.deps import admin_required
from bookland.interfaces.api.docs import (
    SERIES_SUCCESS_RESPONSE,
    SERIES_NOT_FOUND_RESPONSE,
    ALL_SERIES_SUCCESS_RESPONSE,
    FORBIDDEN_RESPONSE,
    USER_BAD_REQUEST,
    USER_UNAUTHORIZED,
    EMPTY_SUCCESS_RESPONSE,
)
from bookland.interfaces.api.responses import empty_search_result_response
from bookland.interfaces.api.exceptions import series_not_found_exception


router = APIRouter(
    dependencies=[Depends(admin_required)],
    responses={**FORBIDDEN_RESPONSE, **USER_UNAUTHORIZED},
)


@router.post(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**USER_BAD_REQUEST, **SERIES_SUCCESS_RESPONSE},
)
async def create_series(series: CreateSeriesSchema):
    new_series = Series(
        str(uuid4()), Title(series.name), Slug(series.slug), series.description
    )

    created_series = await create_series_usecase.execute(new_series)

    return ResponseEnvelopeSchema(
        message="Série cadastrada com sucesso.",
        data={"series": SeriesResponseSchema.from_entity(created_series)},
    )


@router.get(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**ALL_SERIES_SUCCESS_RESPONSE},
)
async def get_all_series():
    all_series = await get_all_series_usecase.execute()

    if len(all_series) == 0:
        return empty_search_result_response()

    return ResponseEnvelopeSchema(
        message="Séries encontradas.",
        data={
            "all_series": [
                SeriesResponseSchema.from_entity(series) for series in all_series
            ]
        },
    )


@router.get(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**SERIES_SUCCESS_RESPONSE, **SERIES_NOT_FOUND_RESPONSE},
)
async def get_series(id: str):
    series = await _get_existing_series_or_404(id)

    return ResponseEnvelopeSchema(
        message="Série encontrada.",
        data={"series": SeriesResponseSchema.from_entity(series)},
    )


@router.patch(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**SERIES_SUCCESS_RESPONSE, **SERIES_NOT_FOUND_RESPONSE},
)
async def update_series(id: str, series: UpdateSeriesSchema):
    await _get_existing_series_or_404(id)

    updated_series = await update_series_usecase.execute(
        Series(id, Title(series.name), Slug(series.slug), series.description)
    )

    return ResponseEnvelopeSchema(
        message="Série editada com sucesso.",
        data={"series": SeriesResponseSchema.from_entity(updated_series)},
    )


@router.delete(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**SERIES_NOT_FOUND_RESPONSE, **EMPTY_SUCCESS_RESPONSE},
)
async def delete_series(id: str):
    series = await _get_existing_series_or_404(id)
    await soft_delete_series_usecase.execute(id)

    return ResponseEnvelopeSchema(
        message="Série excluída com sucesso.",
        data={"series": SeriesResponseSchema.from_entity(series)},
    )


async def _get_existing_series_or_404(id: str) -> Series:
    series = await get_series_usecase.execute(id)

    if not series:
        raise series_not_found_exception()

    return series
