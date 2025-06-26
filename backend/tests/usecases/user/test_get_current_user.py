from bookland.infra.repositories.in_memory_user_repository import InMemoryUserRepository
from bookland.usecases.user.get_current_user import GetCurrentUserUseCase
from tests.factories.user_factory import create_user


def test_get_current_user_successfully():
    repository = InMemoryUserRepository()
    usecase = GetCurrentUserUseCase(repository)

    user = create_user()
    repository.register(user)

    assert usecase.execute() == user
