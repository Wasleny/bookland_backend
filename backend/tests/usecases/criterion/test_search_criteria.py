from bookland.infra.repositories.in_memory_criterion_repository import (
    InMemoryCriterionRepository,
)
from bookland.usecases.criterion.search_criteria import SearchCriteriaUseCase
from tests.factories.criterion_factory import create_criterion


def test_search_criteria_matches_search():
    repository = InMemoryCriterionRepository()
    usecase = SearchCriteriaUseCase(repository)

    criterion = create_criterion()
    repository.create(criterion)

    criteria_found = usecase.execute("Ritmo")

    assert len(criteria_found) == 1


def test_search_criteria_returns_empty_when_no_match():
    repository = InMemoryCriterionRepository()
    usecase = SearchCriteriaUseCase(repository)

    criterion = create_criterion()
    repository.create(criterion)

    criteria_found = usecase.execute("Test")

    assert len(criteria_found) == 0
