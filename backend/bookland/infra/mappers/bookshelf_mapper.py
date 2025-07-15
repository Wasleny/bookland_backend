from bookland.domain.entities import Bookshelf
from bookland.domain.value_objects import Label, Slug
from bookland.infra.mongo_models import BookshelfDocument


class BookshelfMapper:
    @staticmethod
    def to_domain(document: BookshelfDocument) -> Bookshelf:
        return Bookshelf(
            id=document.id, name=Label(document.name), slug=Slug(document.slug)
        )

    @staticmethod
    def to_document(bookshelf: Bookshelf) -> BookshelfDocument:
        return BookshelfDocument(
            id=bookshelf.id, name=bookshelf.name.value, slug=bookshelf.slug.value
        )
