from bookland.infra.repositories.in_memory_criterion_repository import (
    InMemoryCriterionRepository,
)
from bookland.usecases.criterion.update_criterion import UpdateCriterionUseCase
from tests.factories.criterion_factory import create_criterion

def test_update_criterion_updates_criterion_data():
    repository = InMemoryCriterionRepository()
    usecase = UpdateCriterionUseCase(repository)

    criterion = create_criterion()
    repository.create(criterion)

    updated_data = create_criterion(id=criterion.id, user_id='2')

    usecase.execute(updated_data)

    updated_criterion = repository.get_by_id(criterion.id)

    assert updated_criterion.user_id == '2'
    assert updated_criterion.name.value == "Ritmo"