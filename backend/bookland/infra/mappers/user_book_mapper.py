from bookland.domain.entities import UserBook
from bookland.infra.mongo_models import UserBookDocument


class UserBookMapper:
    @staticmethod
    def to_domain(document: UserBookDocument) -> UserBook:
        return UserBook(
            id=document.id,
            book_id=document.book_id,
            user_id=document.user_id,
            default_bookshelf_id=document.default_bookshelf_id,
        )

    @staticmethod
    def to_document(user_book: UserBook) -> UserBookDocument:
        return UserBookDocument(
            id=user_book.id,
            book_id=user_book.book_id,
            user_id=user_book.user_id,
            default_bookshelf_id=user_book.default_bookshelf_id,
        )
