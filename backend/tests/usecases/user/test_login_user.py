from bookland.infra.repositories.in_memory_user_repository import InMemoryUserRepository
from bookland.usecases.user.login_user import LoginUserUseCase
from tests.factories.user_factory import create_user


def test_login_user_succeeds_with_valid_credentials():
    repository = InMemoryUserRepository()
    usecase = LoginUserUseCase(repository)

    user = create_user()
    repository.register(user)
    current_user = usecase.execute(user.email, user.password)

    assert user == current_user
    assert repository.get_current_user() == user


def test_login_user_fails_with_invalid_credentials():
    repository = InMemoryUserRepository()
    usecase = LoginUserUseCase(repository)

    user = create_user()
    current_user = usecase.execute(user.email, user.password)

    assert current_user is None
    assert repository.get_current_user() is None