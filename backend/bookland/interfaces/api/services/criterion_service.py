from bookland.infra.repositories import MongoCriterionRepository
from bookland.application.usecases import (
    CreateCriterionUseCase,
    GetAllCriteriaUseCase,
    GetCriterionByIdUseCase,
    SearchCriteriaUseCase,
    SoftDeleteCriterionUseCase,
    UpdateCriterionUseCase,
)


repository = MongoCriterionRepository()

create_criterion_usecase = CreateCriterionUseCase(repository)
get_all_criteria_usecase = GetAllCriteriaUseCase(repository)
get_criterion_usecase = GetCriterionByIdUseCase(repository)
search_criteria_usecase = SearchCriteriaUseCase(repository)
soft_delete_criterion_usecase = SoftDeleteCriterionUseCase(repository)
update_criterion_usecase = UpdateCriterionUseCase(repository)
