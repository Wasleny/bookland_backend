from bookland.infra.repositories.in_memory_user_repository import InMemoryUserRepository
from bookland.usecases.user.register_user import RegisterUserUseCase
from tests.factories.user_factory import create_user

def test_register_user_succeeds_with_valid_credentials():
    repository = InMemoryUserRepository()
    usecase = RegisterUserUseCase(repository)

    user = create_user()
    current_user = usecase.execute(user)

    assert user == current_user
    assert repository.get_current_user() == user