from bookland.domain.value_objects.name_vo import Name
from bookland.domain.value_objects.label_vo import Label
from bookland.domain.value_objects.isbn_vo import Isbn
from bookland.domain.value_objects.date_vo import Date
from bookland.domain.enums.book_format import BookFormat
from bookland.domain.exceptions.book_exception import InvalidBookException
from datetime import datetime


class Book:
    def __init__(
        self,
        id: str,
        title: Name,
        author_ids: list[str],
        main_genre_id: str,
        cover: str,
        synopsis: str,
        format: BookFormat,
        pages: int,
        publication_date: Date,
        language: str,
        original_title: Name,
        secondary_genre_ids: list = [],
        trope_ids: list = [],
        series_id: str | None = None,
        original_series_id: str | None = None,
        book_number: float | None = None,
        publisher: str | None = None,
        isbn10: Isbn | None = None,
        isbn13: Isbn | None = None,
        asin: str | None = None,
    ):
        self._validate_book(
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
            secondary_genre_ids,
            trope_ids,
            series_id,
            original_series_id,
            book_number,
            publisher,
            isbn10,
            isbn13,
            asin,
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
        self._average_rating = None
        self._reviews_count = None
        self._ratings_count = None
        self._synopsis = synopsis
        self._format = format
        self._pages = pages
        self._publication_date = publication_date
        self._publisher = publisher
        self._isbn10 = isbn10
        self._isbn13 = isbn13
        self._asin = asin
        self._language = language
        self._edition_count = 1
        self._deleted_at = None

    @staticmethod
    def _validate_book(
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
        secondary_genre_ids,
        trope_ids,
        series_id,
        original_series_id,
        book_number,
        publisher,
        isbn10,
        isbn13,
        asin,
    ):
        Book._validate_title(title)
        Book._validate_author_ids(author_ids)
        Book._validate_main_genre_id(main_genre_id)
        Book._validate_cover(cover)
        Book._validate_synopsis(synopsis)
        Book._validate_format(format)
        Book._validate_pages(pages)
        Book._validate_publication_date(publication_date)
        Book._validate_language(language)
        Book._validate_original_title(original_title)
        Book._validate_secondary_genre_ids(secondary_genre_ids)
        Book._validate_trope_ids(trope_ids)
        Book._validate_series_id(series_id)
        Book._validate_original_series_id(original_series_id)
        Book._validate_book_number(book_number)
        Book._validate_publisher(publisher)
        Book._validate_isbn(isbn10)
        Book._validate_isbn(isbn13)
        Book._validate_asin(asin)

    @staticmethod
    def _validate_asin(asin):
        if asin is None:
            return

        if not isinstance(asin, str) or len(asin) != 10:
            raise InvalidBookException(
                "ASIN deve ser uma string e ter tamanho igual a 10"
            )

    @staticmethod
    def _validate_isbn(isbn):
        if isbn is None:
            return

        if not isinstance(isbn, Isbn):
            raise InvalidBookException("ISBN deve ser uma instância de Isbn")

    @staticmethod
    def _validate_publisher(publisher):
        if publisher is None:
            return

        if not isinstance(publisher, str) or len(publisher) < 1:
            raise InvalidBookException(
                "A editora deve ser uma string e ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_book_number(book_number):
        if book_number is None:
            return

        if not isinstance(book_number, float) or book_number <= 0:
            raise InvalidBookException(
                "O número do livro deve ser um float e maior que zero"
            )

    @staticmethod
    def _validate_original_series_id(series_id):
        if series_id is None:
            return

        if not isinstance(series_id, str) or len(series_id) < 1:
            raise InvalidBookException(
                "Id da série original deve ser uma string e ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_series_id(series_id):
        if series_id is None:
            return

        if not isinstance(series_id, str) or len(series_id) < 1:
            raise InvalidBookException(
                "Id da série deve ser uma string e ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_trope_ids(trope_ids):
        if not isinstance(trope_ids, list):
            raise InvalidBookException("Tropes deve ser uma lista")

    @staticmethod
    def _validate_secondary_genre_ids(secondary_genre_ids):

        if not isinstance(secondary_genre_ids, list):
            raise InvalidBookException("Gêneros secondários deve ser uma lista")

    @staticmethod
    def _validate_original_title(original_title):
        if not isinstance(original_title, Name):
            raise InvalidBookException("Idioma deve ser uma instância de Name")

    @staticmethod
    def _validate_language(language):
        if not isinstance(language, str) or len(language) < 1:
            raise InvalidBookException(
                "Idioma deve ser uma string e ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_publication_date(publication_date):
        if not isinstance(publication_date, Date):
            raise InvalidBookException(
                "Data de publicação deve ser uma instância de Date"
            )

    @staticmethod
    def _validate_pages(pages):
        if not isinstance(pages, int) or pages <= 0:
            raise InvalidBookException("Formato deve ser um inteiro")

    @staticmethod
    def _validate_format(format):
        if not isinstance(format, BookFormat):
            raise InvalidBookException("Formato deve ser uma instância de BookFormat")

    @staticmethod
    def _validate_synopsis(synopsis):
        if not isinstance(synopsis, str) or len(synopsis) < 1:
            raise InvalidBookException(
                "Sinopse deve ser uma string e deve ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_cover(cover):
        if not isinstance(cover, str) or len(cover) < 1:
            raise InvalidBookException(
                "Capa deve ser uma string e deve ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_main_genre_id(main_genre_id):
        if not isinstance(main_genre_id, str) or len(main_genre_id) < 1:
            raise InvalidBookException(
                "Gênero principal deve ser uma string e deve ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_author_ids(author_ids):
        if not isinstance(author_ids, list) or len(author_ids) < 1:
            raise InvalidBookException(
                "Nome do livro deve ser uma lista e deve ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_title(title):
        if not isinstance(title, Name) or len(title.value) < 1:
            raise InvalidBookException(
                "Nome do livro deve ser uma instância de Name e deve ter tamanho maior que zero"
            )

    def soft_delete(self):
        if not self.is_deleted:
            self._deleted_at = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title.value

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
        return self._publication_date.value

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
        return self._isbn10.value

    @property
    def isbn13(self):
        return self._isbn13.value

    @property
    def asin(self):
        return self._asin

    @property
    def is_deleted(self):
        return self._deleted_at is not None

    @property
    def deleted_at(self):
        return self._deleted_at
