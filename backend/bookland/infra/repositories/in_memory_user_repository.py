from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository
from bookland.domain.enums.user_role import UserRole


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users: dict[str, User] = {}
        self._current_user_id: str = None

    def login(self, email: str, password: str) -> User | None:
        for user in self._users.values():
            if user.email == email and user.password == password:
                self._current_user_id = user.id
                return user

        return None

    def register(self, user: User) -> User:
        self._users[user.id] = user
        self._current_user_id = user.id

        return user

    def logout(self) -> None:
        self._current_user_id = None

    def get_current_user(self) -> User | None:
        return self._users.get(self._current_user_id) if self._current_user_id else None

    def set_current_user(self, user: User) -> None:
        self._users[user.id] = user
        self._current_user_id = user.id

    def promote_to_admin(self, user: User) -> None:
        if user.id in self._users:
            self._users[user.id].promote_to_admin()

    def demote_from_admin(self, user: User) -> None:
        if user.id in self._users:
            self._users[user.id].demote_to_admin()

    def search(self, search_term: str) -> User | None:
        for user in self._users.values():
            if user.email.value == search_term:
                return user

        return None

    def get_by_id(self, user_id: str) -> User:
        return self._users.get(user_id)
