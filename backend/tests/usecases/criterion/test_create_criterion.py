from bookland.infra.repositories.in_memory_criterion_repository import (
    InMemoryCriterionRepository,
)
from bookland.usecases.criterion.create_criterion import CreateCriterionUseCase
from tests.factories.criterion_factory import create_criterion


def test_create_criterion_creates_criterion_successfully():
    repository = InMemoryCriterionRepository()
    usecase = CreateCriterionUseCase(repository)
    criterion = create_criterion()

    usecase.execute(criterion)

    assert repository.get_by_id(criterion.id) == criterion
