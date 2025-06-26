from bookland.infra.repositories.in_memory_user_repository import InMemoryUserRepository
from bookland.usecases.user.search_user import SearchUserUseCase
from tests.factories.user_factory import create_user


def test_search_user_returns_user():
    repository = InMemoryUserRepository()
    usecase = SearchUserUseCase(repository)

    user = create_user()
    repository.register(user)

    assert usecase.execute(user.email.value) == user


def test_search_user_returns_none_when_not_found():
    repository = InMemoryUserRepository()
    usecase = SearchUserUseCase(repository)

    user = create_user()
    repository.register(user)

    assert usecase.execute("invalid-email") is None
