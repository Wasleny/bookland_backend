from abc import ABC, abstractmethod
from bookland.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def login(self, email: str, password: str) -> User | None: ...

    @abstractmethod
    def register(self, user: User) -> User: ...

    @abstractmethod
    def logout(self) -> None: ...

    @abstractmethod
    def get_current_user(self) -> User | None: ...

    @abstractmethod
    def set_current_user(self, user: User) -> None: ...

    @abstractmethod
    def promote_to_admin(self, user: User) -> None: ...

    @abstractmethod
    def demote_from_admin(self, user: User) -> None: ...

    @abstractmethod
    def search(self, search_term: str) -> User | None: ...

    @abstractmethod
    def get_by_id(self, user_id: str) -> User | None: ...
