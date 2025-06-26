from bookland.infra.repositories.in_memory_criterion_repository import (
    InMemoryCriterionRepository,
)
from bookland.usecases.criterion.get_criterion_by_id import GetCriterionByIdUseCase
from tests.factories.criterion_factory import create_criterion


def test_get_criterion_by_id_returns_criterion_when_found():
    repository = InMemoryCriterionRepository()
    usecase = GetCriterionByIdUseCase(repository)

    criterion = create_criterion()
    repository.create(criterion)

    criterion_found = usecase.execute(criterion.id)

    assert criterion == criterion_found


def test_get_criterion_by_id_returns_none_when_not_found():
    repository = InMemoryCriterionRepository()
    usecase = GetCriterionByIdUseCase(repository)

    criterion_found = usecase.execute("invalid-id")

    assert criterion_found is None
