from bookland.domain.entities import UserBook
from bookland.domain.repositories import UserBookRepository


class InMemoryUserBookRepository(UserBookRepository):
    def __init__(self) -> None:
        self._user_book: dict[str, UserBook] = {}

    async def get_by_user(self, user_id: str) -> list[UserBook]:
        return [entry for entry in self._user_book.values() if entry.user_id == user_id]

    async def get_by_user_and_book(self, user_id: str, book_id: str) -> UserBook | None:
        for user_book in self._user_book.values():
            if user_book.book_id == book_id and user_book.user_id == user_id:
                return user_book

        return None

    async def create(self, user_book: UserBook) -> UserBook:
        self._user_book[user_book.id] = user_book

        return user_book

    async def update(self, user_book: UserBook) -> UserBook | None:
        if user_book.id in self._user_book:
            self._user_book[user_book.id] = user_book
            return user_book

        return None

    async def delete(self, user_book_id: str) -> UserBook | None:
        if user_book_id in self._user_book:
            user_book = self._user_book.get(user_book_id)
            self._user_book.pop(user_book_id, None)
            return user_book

        return None

    async def get_by_id(self, user_book_id: str) -> UserBook | None:
        return self._user_book.get(user_book_id)
