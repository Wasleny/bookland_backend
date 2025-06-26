from bookland.infra.repositories.in_memory_user_repository import InMemoryUserRepository
from bookland.usecases.user.set_current_user import SetCurrentUserUseCase
from tests.factories.user_factory import create_user


def test_set_current_user_successfully():
    repository = InMemoryUserRepository()
    usecase = SetCurrentUserUseCase(repository)

    user = create_user()
    usecase.execute(user)

    assert repository.get_current_user() == user
