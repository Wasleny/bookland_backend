from bookland.domain.entities import Bookshelf
from bookland.domain.repositories import BookshelfRepository


class InMemoryBookshelfRepository(BookshelfRepository):
    def __init__(self) -> None:
        self._bookshelves: dict[str, Bookshelf] = {}

    async def get_all(self) -> list[Bookshelf]:
        return [bookshelf for bookshelf in self._bookshelves.values()]
