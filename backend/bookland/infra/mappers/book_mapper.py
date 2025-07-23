from bookland.domain.entities import Book
from bookland.domain.value_objects import Title, Isbn, Date, Slug, Rating
from bookland.infra.mongo_models import BookDocument
from bookland.domain.enums import BookFormat


class BookMapper:
    @staticmethod
    def to_domain(document: BookDocument) -> Book:
        return Book(
            id=document.id,
            title=Title(document.title),
            original_title=Title(document.original_title),
            author_ids=document.author_ids,
            main_genre_id=document.main_genre_id,
            secondary_genre_ids=document.secondary_genre_ids,
            trope_ids=document.trope_ids,
            cover=document.cover,
            series_id=document.series_id,
            original_series_id=document.original_series_id,
            book_number=document.book_number,
            average_rating=Rating(
                document.average_rating if document.average_rating != 0.0 else None,
                True,
            ),
            reviews_count=document.reviews_count,
            ratings_count=document.ratings_count,
            synopsis=document.synopsis,
            format=BookFormat(document.format),
            pages=document.pages,
            publication_date=Date(document.publication_date),
            publisher=document.publisher,
            isbn10=Isbn(document.isbn10) if document.isbn10 else None,
            isbn13=Isbn(document.isbn13) if document.isbn13 else None,
            asin=document.asin,
            language=document.language,
            alternative_edition_ids=(
                document.alternative_edition_ids
                if len(document.alternative_edition_ids) > 0
                else None
            ),
            slug=Slug(document.slug),
        )

    @staticmethod
    def to_document(book: Book) -> BookDocument:
        return BookDocument(
            id=book.id,
            title=book.title.value,
            original_title=book.original_title.value,
            author_ids=book.author_ids,
            main_genre_id=book.main_genre_id,
            secondary_genre_ids=book.secondary_genre_ids,
            trope_ids=book.trope_ids,
            cover=book.cover,
            series_id=book.series_id,
            original_series_id=book.original_series_id,
            book_number=book.book_number,
            average_rating=(
                book.average_rating.value
                if book.average_rating.value is not None
                else 0.0
            ),
            reviews_count=book.reviews_count,
            ratings_count=book.ratings_count,
            synopsis=book.synopsis,
            format=book.format,
            pages=book.pages,
            publication_date=book.publication_date.value,
            publisher=book.publisher,
            isbn10=book.isbn10.value if book.isbn10 else None,
            isbn13=book.isbn13.value if book.isbn13 else None,
            asin=book.asin,
            language=book.language,
            alternative_edition_ids=book.alternative_edition_ids or [],
            slug=book.slug.value,
        )
