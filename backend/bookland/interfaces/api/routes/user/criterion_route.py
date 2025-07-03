from fastapi import APIRouter, Depends, Query
from uuid import uuid4

from bookland.domain.entities.criterion import Criterion
from bookland.domain.value_objects import Label
from bookland.interfaces.api.docs import (
    CRITERION_SUCCESS_RESPONSE,
    CRITERION_NOT_FOUND_RESPONSE,
    CRITERIA_SUCCESS_RESPONSE,
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
from bookland.interfaces.api.services.criterion_service import *
from bookland.interfaces.api.responses import (
    bad_request_response,
    empty_search_result_response,
)
from bookland.interfaces.api.exceptions import criterion_not_found_exception


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
    criterion_data: CreateCriterionSchema, current_user=Depends(get_current_user)
):
    criterion = Criterion(
        str(uuid4()),
        Label(criterion_data.name),
        criterion_data.description,
        current_user.id,
    )
    new_criterion = await create_criterion_usecase.execute(criterion)

    return ResponseEnvelopeSchema(
        message="Critério criado com sucesso.",
        data={"criterion": CriterionResponseSchema.from_entity(new_criterion)},
    )


@router.get(
    "/search",
    response_model=ResponseEnvelopeSchema,
    responses={
        **CRITERIA_SUCCESS_RESPONSE,
    },
)
async def search_criteria(
    search_term: str = Query(..., description="Termo de busca para os critérios."),
    current_user=Depends(get_current_user),
):
    criteria = await search_criteria_usecase.execute(search_term, current_user.id)

    if len(criteria) == 0:
        return empty_search_result_response()

    return ResponseEnvelopeSchema(
        message="Critérios encontrados.",
        data={
            "criteria": [
                CriterionResponseSchema.from_entity(criterion) for criterion in criteria
            ]
        },
    )


@router.get(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={
        **CRITERIA_SUCCESS_RESPONSE,
    },
)
async def get_criteria(current_user=Depends(get_current_user)):
    criteria = await get_all_criteria_usecase.execute(current_user.id)

    if len(criteria) == 0:
        return empty_search_result_response()

    return ResponseEnvelopeSchema(
        message="Critérios encontrados.",
        data={
            "criteria": [
                CriterionResponseSchema.from_entity(criterion) for criterion in criteria
            ]
        },
    )


@router.get(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={
        **CRITERION_SUCCESS_RESPONSE,
        **CRITERION_NOT_FOUND_RESPONSE,
    },
)
async def get_criterion(id: str, current_user=Depends(get_current_user)):
    criterion = await _verify_ownership(id, current_user)

    return ResponseEnvelopeSchema(
        message="Critério encontrado.",
        data={"criterion": CriterionResponseSchema.from_entity(criterion)},
    )


@router.delete(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**CRITERION_NOT_FOUND_RESPONSE, **EMPTY_SUCCESS_RESPONSE},
)
async def delete_criterion(id: str, current_user=Depends(get_current_user)):
    await _verify_ownership(id, current_user)
    await soft_delete_criterion_usecase.execute(id)

    return ResponseEnvelopeSchema(message="Critério excluído com sucesso.", data={})


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
):
    await _verify_ownership(id, current_user)

    criterion = Criterion(
        id,
        Label(criterion_data.name),
        criterion_data.description,
        current_user.id,
    )
    updated_criterion = await update_criterion_usecase.execute(criterion)

    return ResponseEnvelopeSchema(
        message="Critério atualizado com sucesso.",
        data={"criterion": CriterionResponseSchema.from_entity(updated_criterion)},
    )


async def _verify_ownership(criterion_id: str, current_user) -> Criterion:
    criterion = await _verify_existence(criterion_id)
    await owner_required(criterion.user_id, current_user)

    return criterion


async def _verify_existence(id: str) -> Criterion:
    criterion = await get_criterion_usecase.execute(id)

    if not criterion:
        raise criterion_not_found_exception()

    return criterion
