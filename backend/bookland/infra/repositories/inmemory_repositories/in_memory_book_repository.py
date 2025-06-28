from bookland.domain.entities.book import Book
from bookland.domain.repositories.book_repository import BookRepository
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

    async def search(self, search_term: str) -> list[Book]:
        normalized_search = normalize_text(search_term)

        return [
            book
            for book in self._books.values()
            if not book.is_deleted and self._matches_search(book, normalized_search)
        ]

    async def create(self, book: Book) -> Book:
        self._books[book.id] = book

        return book

    async def update(self, book: Book) -> Book | None:
        if book.id in self._books:
            self._books[book.id] = book
            return book

        return None

    async def soft_delete(self, book_id: str) -> None:
        book = self._books.get(book_id)

        if book:
            book.soft_delete()

    @staticmethod
    def _matches_search(book: Book, normalized_search: str) -> bool:
        asin = getattr(book, "asin", "")
        isbn10 = getattr(book, "isbn10", "")
        isbn13 = getattr(book, "isbn13", "")

        normalized_title = normalize_text(getattr(book, "title", ""))
        normalized_series = normalize_text(getattr(book, "series", ""))
        normalized_original_series = normalize_text(
            getattr(book, "original_series", "")
        )
        normalized_authors = [
            normalize_text(author) for author in getattr(book, "normalized_authors", [])
        ]

        searchable_fields = [
            asin,
            isbn10,
            isbn13,
            normalized_title,
            normalized_series,
            normalized_original_series,
        ]

        if any(normalized_search in field for field in searchable_fields) or any(
            normalized_search in author for author in normalized_authors
        ):
            return True

        return False
