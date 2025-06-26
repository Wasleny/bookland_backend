from bookland.infra.repositories.in_memory_user_repository import InMemoryUserRepository
from bookland.usecases.user.get_user_by_id import GetUserByIdUseCase
from tests.factories.user_factory import create_user

def test_get_user_by_id_returns_user():
    repository = InMemoryUserRepository()
    usecase = GetUserByIdUseCase(repository)

    user = create_user()
    repository.register(user)

    assert usecase.execute(user.id) == user

def test_get_user_by_id_returns_none_when_not_found():
    repository = InMemoryUserRepository()
    usecase = GetUserByIdUseCase(repository)

    user = create_user()
    repository.register(user)

    assert usecase.execute('invalid-id') is None
