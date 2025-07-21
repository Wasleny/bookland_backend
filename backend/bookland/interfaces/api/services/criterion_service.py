from fastapi import Depends

from bookland.infra.repositories import MongoCriterionRepository
from bookland.application.usecases import (
    CreateCriterionUseCase,
    GetAllCriteriaUseCase,
    GetCriterionByIdUseCase,
    SearchCriteriaUseCase,
    SoftDeleteCriterionUseCase,
    UpdateCriterionUseCase,
)


def get_criterion_repository() -> MongoCriterionRepository:
    return MongoCriterionRepository()


def get_create_criterion_usecase(
    repository: MongoCriterionRepository = Depends(get_criterion_repository),
) -> CreateCriterionUseCase:
    return CreateCriterionUseCase(repository)


def get_get_all_criteria_usecase(
    repository: MongoCriterionRepository = Depends(get_criterion_repository),
) -> GetAllCriteriaUseCase:
    return GetAllCriteriaUseCase(repository)


def get_get_criterion_usecase(
    repository: MongoCriterionRepository = Depends(get_criterion_repository),
) -> GetCriterionByIdUseCase:
    return GetCriterionByIdUseCase(repository)


def get_search_criteria_usecase(
    repository: MongoCriterionRepository = Depends(get_criterion_repository),
) -> SearchCriteriaUseCase:
    return SearchCriteriaUseCase(repository)


def get_soft_delete_criterion_usecase(
    repository: MongoCriterionRepository = Depends(get_criterion_repository),
) -> SoftDeleteCriterionUseCase:
    return SoftDeleteCriterionUseCase(repository)


def get_update_criterion_usecase(
    repository: MongoCriterionRepository = Depends(get_criterion_repository),
) -> UpdateCriterionUseCase:
    return UpdateCriterionUseCase(repository)
