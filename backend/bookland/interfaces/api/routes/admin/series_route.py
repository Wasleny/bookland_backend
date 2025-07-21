from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from uuid import uuid4

from bookland.domain.entities import Series
from bookland.domain.value_objects import Title, Slug
from bookland.interfaces.api.services import (
    get_create_series_usecase,
    get_get_all_series_usecase,
    get_get_series_usecase,
    get_update_series_usecase,
    get_soft_delete_series_usecase,
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
from bookland.interfaces.api.messages import series_messages


router = APIRouter(
    dependencies=[Depends(admin_required)],
    responses={**FORBIDDEN_RESPONSE, **USER_UNAUTHORIZED},
)


@router.post(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**USER_BAD_REQUEST, **SERIES_SUCCESS_RESPONSE},
)
async def create_series(
    series: CreateSeriesSchema, usecase=Depends(get_create_series_usecase)
):
    new_series = Series(
        str(uuid4()), Title(series.name), Slug(series.slug), series.description
    )

    created_series = await usecase.execute(new_series)

    JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=series_messages.CREATE_SERIES_MESSAGE,
            data={"series": SeriesResponseSchema.from_entity(created_series)},
        ).model_dump(),
    )


@router.get(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**ALL_SERIES_SUCCESS_RESPONSE},
)
async def get_all_series(usecase=Depends(get_get_all_series_usecase)):
    all_series = await usecase.execute()

    if len(all_series) == 0:
        return empty_search_result_response()

    JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=series_messages.GET_ALL_SERIES_MESSAGE,
            data={
                "all_series": [
                    SeriesResponseSchema.from_entity(series) for series in all_series
                ]
            },
        ).model_dump(),
    )


@router.get(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**SERIES_SUCCESS_RESPONSE, **SERIES_NOT_FOUND_RESPONSE},
)
async def get_series(
    id: str,
    get_series=Depends(get_get_series_usecase),
):
    series = await _get_existing_series_or_404(id, get_series)

    return ResponseEnvelopeSchema(
        message=series_messages.GET_SERIES_MESSAGE,
        data={"series": SeriesResponseSchema.from_entity(series)},
    )


@router.patch(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**SERIES_SUCCESS_RESPONSE, **SERIES_NOT_FOUND_RESPONSE},
)
async def update_series(
    id: str,
    series: UpdateSeriesSchema,
    usecase=Depends(get_update_series_usecase),
    get_series=Depends(get_get_series_usecase),
):
    await _get_existing_series_or_404(id, get_series)

    updated_series = await usecase.execute(
        Series(id, Title(series.name), Slug(series.slug), series.description)
    )

    return ResponseEnvelopeSchema(
        message=series_messages.UPDATE_SERIES_MESSAGE,
        data={"series": SeriesResponseSchema.from_entity(updated_series)},
    )


@router.delete(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**SERIES_NOT_FOUND_RESPONSE, **EMPTY_SUCCESS_RESPONSE},
)
async def delete_series(
    id: str,
    usecase=Depends(get_soft_delete_series_usecase),
    get_series=Depends(get_get_series_usecase),
):
    series = await _get_existing_series_or_404(id, get_series)
    await usecase.execute(id)

    return ResponseEnvelopeSchema(
        message=series_messages.DELETE_SERIES_MESSAGE,
        data={"series": SeriesResponseSchema.from_entity(series)},
    )


async def _get_existing_series_or_404(id: str, get_series) -> Series:
    series = await get_series.execute(id)

    if not series:
        raise series_not_found_exception()

    return series
