from bookland.domain.entities import Bookshelf
from bookland.domain.repositories import BookshelfRepository


class InMemoryBookshelfRepository(BookshelfRepository):
    def __init__(self) -> None:
        self._bookshelves: dict[str, Bookshelf] = {
            "1": {"id": "1", "name": "Lidos", "slug": "lidos"},
            "2": {"id": "2", "name": "Quero ler", "slug": "quero-ler"},
        }

    async def get_all(self) -> list[Bookshelf]:
        return [bookshelf for bookshelf in self._bookshelves.values()]
