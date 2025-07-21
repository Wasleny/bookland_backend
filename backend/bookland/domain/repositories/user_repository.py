from abc import ABC, abstractmethod

from bookland.domain.entities import User
from bookland.domain.value_objects import Email, Password
from bookland.domain.enums import UserRole


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
    async def promote_to_admin(self, user_id: str) -> User | None: ...

    @abstractmethod
    async def demote_from_admin(self, user_id: str) -> User | None: ...

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None: ...

    @abstractmethod
    async def get_by_id(self, user_id: str) -> User | None: ...

    @abstractmethod
    async def get_by_role(self, role: UserRole) -> list[User]: ...
