from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository
from bookland.domain.value_objects.email_vo import Email
from bookland.domain.value_objects.password_vo import Password


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._users: dict[str, User] = {}
        self._current_user_id: str | None = None

    async def login(self, email: Email, password: Password) -> User | None:
        for user in self._users.values():
            if user.email == email and user.password == password:
                self._current_user_id = user.id
                return user

        return None

    async def register(self, user: User) -> User:
        self._users[user.id] = user
        self._current_user_id = user.id

        return user

    async def logout(self) -> None:
        self._current_user_id = None

    async def get_current_user(self) -> User | None:
        return self._users.get(self._current_user_id) if self._current_user_id else None

    async def set_current_user(self, user_id) -> None:
        user = self._users.get(user_id)
        self._current_user_id = user.id if user else None

    async def promote_to_admin(self, user: User) -> User | None:
        if user.id in self._users:
            self._users[user.id].promote_to_admin()
            return self._users[user.id]

        return None

    async def demote_from_admin(self, user: User) -> User | None:
        if user.id in self._users:
            self._users[user.id].demote_to_admin()
            return self._users[user.id]

        return None

    async def search(self, search_term: str) -> User | None:
        for user in self._users.values():
            if user.email.value == search_term:
                return user

        return None

    async def get_by_id(self, user_id: str) -> User | None:
        return self._users.get(user_id)
