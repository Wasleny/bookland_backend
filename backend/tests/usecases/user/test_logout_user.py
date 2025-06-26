from bookland.infra.repositories.in_memory_user_repository import InMemoryUserRepository
from bookland.usecases.user.logout_user import LogoutUserUseCase
from tests.factories.user_factory import create_user


def test_logout_user_successfully():
    repository = InMemoryUserRepository()
    usecase = LogoutUserUseCase(repository)

    user = create_user()
    repository.register(user)
    usecase.execute()

    assert repository.get_current_user() is None
