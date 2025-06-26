from bookland.domain.value_objects.email_vo import Email
from bookland.domain.value_objects.password_vo import Password
from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository


class LoginUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, email: Email, password: Password) -> User | None:
        return self._repository.login(email, password)
