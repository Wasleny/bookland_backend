from bookland.infra.repositories.in_memory_criterion_repository import (
    InMemoryCriterionRepository,
)
from bookland.usecases.criterion.soft_delete_criterion import SoftDeleteCriterionUseCase
from tests.factories.criterion_factory import create_criterion


def test_soft_delete_criterion_removes_criterion():
    repository = InMemoryCriterionRepository()
    usecase = SoftDeleteCriterionUseCase(repository)

    criterion = create_criterion()
    repository.create(criterion)

    usecase.execute(criterion.id)

    assert repository.get_by_id(criterion.id) is None
