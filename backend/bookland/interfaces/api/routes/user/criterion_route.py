from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import JSONResponse
from uuid import uuid4

from bookland.domain.entities.criterion import Criterion
from bookland.domain.value_objects import Label
from bookland.interfaces.api.docs import (
    CRITERION_SUCCESS_RESPONSE,
    CRITERION_NOT_FOUND_RESPONSE,
    ALL_CRITERIA_SUCCESS_RESPONSE,
    FORBIDDEN_RESPONSE,
    EMPTY_SUCCESS_RESPONSE,
)
from bookland.interfaces.api.schemas import (
    CriterionResponseSchema,
    CreateCriterionSchema,
    UpdateCriterionSchema,
    ResponseEnvelopeSchema,
)
from bookland.interfaces.api.deps import owner_required, get_current_user
from bookland.interfaces.api.services import (
    get_create_criterion_usecase,
    get_get_criterion_usecase,
    get_update_criterion_usecase,
    get_soft_delete_criterion_usecase,
    get_search_criteria_usecase,
    get_get_all_criteria_usecase,
)
from bookland.interfaces.api.responses import empty_search_result_response
from bookland.interfaces.api.exceptions import criterion_not_found_exception
from bookland.interfaces.api.messages import criterion_messages


router = APIRouter(
    responses={
        **FORBIDDEN_RESPONSE,
    },
)


@router.post(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={
        **CRITERION_SUCCESS_RESPONSE,
    },
)
async def create_criterion(
    criterion_data: CreateCriterionSchema,
    current_user=Depends(get_current_user),
    usecase=Depends(get_create_criterion_usecase),
):
    criterion = Criterion(
        str(uuid4()),
        Label(criterion_data.name),
        criterion_data.description,
        current_user.id,
    )
    new_criterion = await usecase.execute(criterion)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=criterion_messages.CREATE_CRITERION_MESSAGE,
            data={"criterion": CriterionResponseSchema.from_entity(new_criterion)},
        ).model_dump(),
    )


@router.get(
    "/search",
    response_model=ResponseEnvelopeSchema,
    responses={
        **ALL_CRITERIA_SUCCESS_RESPONSE,
    },
)
async def search_criteria(
    search_term: str = Query(..., description="Termo de busca para os critérios."),
    current_user=Depends(get_current_user),
    usecase=Depends(get_search_criteria_usecase),
):
    criteria = await usecase.execute(search_term, current_user.id)

    if len(criteria) == 0:
        return empty_search_result_response()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=criterion_messages.GET_ALL_CRITERIA_MESSAGE,
            data={
                "criteria": [
                    CriterionResponseSchema.from_entity(criterion)
                    for criterion in criteria
                ]
            },
        ).model_dump(),
    )


@router.get(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={
        **ALL_CRITERIA_SUCCESS_RESPONSE,
    },
)
async def get_criteria(
    current_user=Depends(get_current_user),
    usecase=Depends(get_get_all_criteria_usecase),
):
    criteria = await usecase.execute(current_user.id)

    if len(criteria) == 0:
        return empty_search_result_response()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=criterion_messages.GET_ALL_CRITERIA_MESSAGE,
            data={
                "criteria": [
                    CriterionResponseSchema.from_entity(criterion)
                    for criterion in criteria
                ]
            },
        ).model_dump(),
    )


@router.get(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={
        **CRITERION_SUCCESS_RESPONSE,
        **CRITERION_NOT_FOUND_RESPONSE,
    },
)
async def get_criterion(
    id: str,
    current_user=Depends(get_current_user),
    get_criterion=Depends(get_get_criterion_usecase),
):
    criterion = await _verify_ownership(id, current_user, get_criterion)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=criterion_messages.GET_CRITERION_MESSAGE,
            data={"criterion": CriterionResponseSchema.from_entity(criterion)},
        ).model_dump(),
    )


@router.delete(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**CRITERION_NOT_FOUND_RESPONSE, **EMPTY_SUCCESS_RESPONSE},
)
async def delete_criterion(
    id: str,
    current_user=Depends(get_current_user),
    usecase=Depends(get_soft_delete_criterion_usecase),
    get_criterion=Depends(get_get_criterion_usecase),
):
    await _verify_ownership(id, current_user, get_criterion)
    await usecase.execute(id)

    JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=criterion_messages.DELETE_CRITERION_MESSAGE, data={}
        ).model_dump(),
    )


@router.patch(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={
        **CRITERION_SUCCESS_RESPONSE,
        **CRITERION_NOT_FOUND_RESPONSE,
    },
)
async def update_criterion(
    id: str,
    criterion_data: UpdateCriterionSchema,
    current_user=Depends(get_current_user),
    usecase=Depends(get_update_criterion_usecase),
    get_criterion=Depends(get_get_criterion_usecase),
):
    await _verify_ownership(id, current_user, get_criterion)

    criterion = Criterion(
        id,
        Label(criterion_data.name),
        criterion_data.description,
        current_user.id,
    )
    updated_criterion = await usecase.execute(criterion)

    JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=criterion_messages.UPDATE_CRITERION_MESSAGE,
            data={"criterion": CriterionResponseSchema.from_entity(updated_criterion)},
        ).model_dump(),
    )


async def _verify_ownership(criterion_id: str, current_user, get_criterion) -> Criterion:
    criterion = await _verify_existence(criterion_id, get_criterion)
    await owner_required(criterion.user_id, current_user)

    return criterion


async def _verify_existence(id: str, get_criterion) -> Criterion:
    criterion = await get_criterion.execute(id)

    if not criterion:
        raise criterion_not_found_exception()

    return criterion
