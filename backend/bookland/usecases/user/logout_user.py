from bookland.domain.repositories.user_repository import UserRepository


class LogoutUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self) -> None:
        return self._repository.logout()
