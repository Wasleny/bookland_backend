from datetime import datetime

from bookland.domain.value_objects import Title, Isbn, Date, Slug, Rating
from bookland.domain.enums import BookFormat
from bookland.domain.exceptions import InvalidBookException
from bookland.domain.errors import CommonErrors, BookErrors


class Book:
    """
    Entity que representa um livro no sistema

    Inclui os seguintes campos:
    - ID
    - título e título original
    - autores (lista de IDs)
    - gênero principal e gêneros secundários (por ID)
    - tropes associadas (por ID)
    - informações de publicação (editora, data, idioma, ISBN, ASIN)
    - série e número dentro da série
    - formato, quantidade de páginas e sinopse
    - média de avaliação, contagem de resenhas e avaliações
    - edições alternativas
    - estado de exclusão lógica (soft delete)
    - slug
    """

    def __init__(
        self,
        id: str,
        title: Title,
        author_ids: list[str],
        main_genre_id: str,
        cover: str,
        synopsis: str,
        format: BookFormat,
        pages: int,
        publication_date: Date,
        language: str,
        original_title: Title,
        slug: Slug,
        secondary_genre_ids: list[str] = [],
        trope_ids: list[str] = [],
        series_id: str | None = None,
        original_series_id: str | None = None,
        book_number: float | None = None,
        publisher: str | None = None,
        isbn10: Isbn | None = None,
        isbn13: Isbn | None = None,
        asin: str | None = None,
        alternative_edition_ids: list | None = None,
        average_rating: Rating = Rating(None),
        reviews_count: int = 0,
        ratings_count: int = 0,
        deleted_at: datetime | None = None,
    ):
        self._validate(
            id,
            title,
            author_ids,
            main_genre_id,
            cover,
            synopsis,
            format,
            pages,
            publication_date,
            language,
            original_title,
            slug,
            secondary_genre_ids,
            trope_ids,
            series_id,
            original_series_id,
            book_number,
            publisher,
            isbn10,
            isbn13,
            asin,
            alternative_edition_ids,
            average_rating,
            reviews_count,
            ratings_count,
            deleted_at,
        )

        self._id = id
        self._title = title
        self._original_title = original_title
        self._author_ids = author_ids
        self._main_genre_id = main_genre_id
        self._secondary_genre_ids = secondary_genre_ids
        self._trope_ids = trope_ids
        self._cover = cover
        self._series_id = series_id
        self._original_series_id = original_series_id
        self._book_number = book_number
        self._average_rating = average_rating
        self._reviews_count = reviews_count
        self._ratings_count = ratings_count
        self._synopsis = synopsis
        self._format = format
        self._pages = pages
        self._publication_date = publication_date
        self._publisher = publisher
        self._isbn10 = isbn10
        self._isbn13 = isbn13
        self._asin = asin
        self._language = language
        self._alternative_edition_ids = alternative_edition_ids
        self._deleted_at = deleted_at
        self._slug = slug

    def _validate(
        self,
        id: str,
        title: Title,
        author_ids: list,
        main_genre_id: str,
        cover: str,
        synopsis: str,
        format: BookFormat,
        pages: int,
        publication_date: Date,
        language: str,
        original_title: Title,
        slug: Slug,
        secondary_genre_ids: list,
        trope_ids: list,
        series_id: str | None,
        original_series_id: str | None,
        book_number: float | None,
        publisher: str | None,
        isbn10: Isbn | None,
        isbn13: Isbn | None,
        asin: str | None,
        alternative_edition_ids: list | None,
        average_rating: Rating,
        reviews_count: int,
        ratings_count: int,
        deleted_at: datetime | None,
    ) -> None:
        if not isinstance(id, str) or len(id) == 0:
            raise InvalidBookException(CommonErrors.INVALID_ID)

        if not isinstance(title, Title):
            raise InvalidBookException(BookErrors.INVALID_TITLE)

        if not isinstance(author_ids, list) or len(author_ids) == 0:
            raise InvalidBookException(BookErrors.INVALID_AUTHORS)

        if not isinstance(main_genre_id, str) or len(main_genre_id) == 0:
            raise InvalidBookException(BookErrors.INVALID_GENRE)

        if not isinstance(cover, str) or len(cover) == 0:
            raise InvalidBookException(BookErrors.INVALID_COVER)

        if not isinstance(synopsis, str) or len(synopsis) == 0:
            raise InvalidBookException(BookErrors.INVALID_SYNOPSIS)

        if not isinstance(format, BookFormat):
            raise InvalidBookException(BookErrors.INVALID_FORMAT)

        if not isinstance(pages, int) or pages <= 0:
            raise InvalidBookException(BookErrors.INVALID_PAGE_COUNT)

        if not isinstance(publication_date, Date):
            raise InvalidBookException(BookErrors.INVALID_PUBLICATION_DATE)

        if not isinstance(language, str) or len(language) == 0:
            raise InvalidBookException(BookErrors.INVALID_LANGUAGE)

        if not isinstance(original_title, Title):
            raise InvalidBookException(BookErrors.INVALID_ORIGINAL_TITLE)

        if not isinstance(secondary_genre_ids, list):
            raise InvalidBookException(BookErrors.INVALID_SECONDARY_GENRES)

        if not isinstance(trope_ids, list):
            raise InvalidBookException(BookErrors.INVALID_TROPES)

        if series_id is not None and (
            not isinstance(series_id, str) or len(series_id) == 0
        ):
            raise InvalidBookException(BookErrors.INVALID_SERIES_ID)

        if original_series_id is not None and (
            not isinstance(original_series_id, str) or len(original_series_id) == 0
        ):
            raise InvalidBookException(BookErrors.INVALID_ORIGINAL_SERIES_ID)

        if book_number is not None and (
            not isinstance(book_number, float) or book_number <= 0
        ):
            raise InvalidBookException(BookErrors.INVALID_BOOK_NUMBER)

        if publisher is not None and (
            not isinstance(publisher, str) or len(publisher) == 0
        ):
            raise InvalidBookException(BookErrors.INVALID_PUBLISHER)

        self._validate_isbn(isbn10)
        self._validate_isbn(isbn13)

        if asin is not None and (not isinstance(asin, str) or len(asin) != 10):
            raise InvalidBookException(BookErrors.INVALID_ASIN)

        if not isinstance(slug, Slug) or len(slug.value) < 1:
            raise InvalidBookException(CommonErrors.INVALID_SLUG)

        if alternative_edition_ids is not None and (
            not isinstance(alternative_edition_ids, list)
            or len(alternative_edition_ids) == 0
        ):
            raise InvalidBookException(BookErrors.INVALID_ALTERNATIVE_EDITIONS)

        if not isinstance(average_rating, Rating):
            raise InvalidBookException(CommonErrors.INVALID_AVERAGE_RATING)

        if not isinstance(reviews_count, int):
            raise InvalidBookException(CommonErrors.INVALID_REVIEWS_COUNT)

        if not isinstance(ratings_count, int):
            raise InvalidBookException(CommonErrors.INVALID_RATINGS_COUNT)

        if deleted_at is not None and not isinstance(deleted_at, datetime):
            raise InvalidBookException(CommonErrors.INVALID_DELETED_AT)

    def _validate_isbn(self, isbn):
        if isbn is not None and not isinstance(isbn, Isbn):
            raise InvalidBookException(BookErrors.INVALID_ISBN)

    def soft_delete(self):
        if not self.is_deleted:
            self._deleted_at = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author_ids(self):
        return self._author_ids

    @property
    def main_genre_id(self):
        return self._main_genre_id

    @property
    def cover(self):
        return self._cover

    @property
    def synopsis(self):
        return self._synopsis

    @property
    def format(self):
        return self._format

    @property
    def pages(self):
        return self._pages

    @property
    def publication_date(self):
        return self._publication_date

    @property
    def language(self):
        return self._language

    @property
    def original_title(self):
        return self._original_title

    @property
    def secondary_genre_ids(self):
        return self._secondary_genre_ids

    @property
    def trope_ids(self):
        return self._trope_ids

    @property
    def series_id(self):
        return self._series_id

    @property
    def original_series_id(self):
        return self._original_series_id

    @property
    def book_number(self):
        return self._book_number

    @property
    def publisher(self):
        return self._publisher

    @property
    def isbn10(self):
        return self._isbn10

    @property
    def isbn13(self):
        return self._isbn13

    @property
    def asin(self):
        return self._asin

    @property
    def is_deleted(self):
        return self._deleted_at is not None

    @property
    def deleted_at(self):
        return self._deleted_at

    @property
    def alternative_edition_ids(self):
        return self._alternative_edition_ids

    @property
    def slug(self):
        return self._slug

    @property
    def average_rating(self):
        return self._average_rating

    @property
    def reviews_count(self):
        return self._reviews_count

    @property
    def ratings_count(self):
        return self._ratings_count
