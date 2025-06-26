from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository


class PromoteUserToAdminUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, user: User) -> None:
        self._repository.promote_to_admin(user)
