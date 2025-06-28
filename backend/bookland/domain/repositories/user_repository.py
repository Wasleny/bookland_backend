from abc import ABC, abstractmethod
from bookland.domain.entities.user import User
from bookland.domain.value_objects.email_vo import Email
from bookland.domain.value_objects.password_vo import Password


class UserRepository(ABC):
    @abstractmethod
    async def login(self, email: Email, password: Password) -> User | None: ...

    @abstractmethod
    async def register(self, user: User) -> User: ...

    @abstractmethod
    async def logout(self) -> None: ...

    @abstractmethod
    async def get_current_user(self) -> User | None: ...

    @abstractmethod
    async def set_current_user(self, user_id: str) -> None: ...

    @abstractmethod
    async def promote_to_admin(self, user: User) -> User | None: ...

    @abstractmethod
    async def demote_from_admin(self, user: User) -> User | None: ...

    @abstractmethod
    async def search(self, search_term: str) -> User | None: ...

    @abstractmethod
    async def get_by_id(self, user_id: str) -> User | None: ...
