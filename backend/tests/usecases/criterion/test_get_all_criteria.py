from bookland.infra.repositories.in_memory_criterion_repository import (
    InMemoryCriterionRepository,
)
from bookland.usecases.criterion.get_all_criteria import GetAllCriteriaUseCase
from tests.factories.criterion_factory import create_criterion


def test_get_all_criteria_returns_all_criteria():
    repository = InMemoryCriterionRepository()
    usecase = GetAllCriteriaUseCase(repository)

    criterion1 = create_criterion()
    criterion2 = create_criterion()
    repository.create(criterion1)
    repository.create(criterion2)

    criteria = usecase.execute()

    assert len(criteria) == 2
    assert criterion1 in criteria
    assert criterion2 in criteria
