from bookland.domain.entities import Book
from bookland.domain.repositories import BookRepository
from bookland.utils.text_utils import normalize_text


class InMemoryBookRepository(BookRepository):
    def __init__(self) -> None:
        self._books: dict[str, Book] = {}

    async def get_all(self) -> list[Book]:
        return [book for book in self._books.values() if not book.is_deleted]

    async def get_by_id(self, book_id: str) -> Book | None:
        for book in self._books.values():
            if not book.is_deleted and book.id == book_id:
                return book

        return None

    async def search(self, search_terms: dict) -> list[Book]:
        search_terms["title"] = normalize_text(search_terms["title"])

        return [
            book
            for book in self._books.values()
            if not book.is_deleted and self._matches_search(book, search_terms)
        ]

    async def create(self, book: Book) -> Book:
        self._books[book.id] = book

        return book

    async def update(self, book: Book) -> Book | None:
        if book.id in self._books:
            self._books[book.id] = book
            return book

        return None

    async def soft_delete(self, book_id: str) -> Book | None:
        book = self._books.get(book_id)

        if book:
            book.soft_delete()
            return book

        return None

    @staticmethod
    def _matches_search(book: Book, search_terms: dict) -> bool:
        def get_field_value(field_name: str) -> str:
            value = getattr(book, field_name, "")
            return normalize_text(
                value.value if hasattr(value, "value") else value or ""
            )

        for key, search_value in search_terms.items():
            if not search_value:
                continue

            normalized_book_value = get_field_value(key)
            normalized_search_value = normalize_text(search_value)

            if normalized_search_value in normalized_book_value:
                return True

        return False
