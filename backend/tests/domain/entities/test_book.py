import pytest
from datetime import date
from bookland.domain.entities.book import Book
from bookland.domain.value_objects.name_vo import Name
from bookland.domain.value_objects.label_vo import Label
from bookland.domain.value_objects.isbn_vo import Isbn
from bookland.domain.value_objects.date_vo import Date
from bookland.domain.enums.book_format import BookFormat
from bookland.domain.exceptions.book_exception import InvalidBookException


def make_book_data(**overrides):
    base = {
        "id": "1",
        "title": Name("Trono de Vidro"),
        "author_ids": ["1"],
        "main_genre_id": "1",
        "cover": "path/to/image",
        "synopsis": "A magia há muito abandonou Adarlan. Um perverso rei governa, punindo impiedosamente as minorias rebeldes.\n\nAos 18 anos uma prisioneira está cumprindo sua sentença. Ela é uma assassina, e a melhor de Adarlan. Aprisionada e fraca, ela está quase perdendo as esperanças, a sentença de morte é iminente, mas a jovem recebe uma proposta inesperada: representar o príncipe em uma competição com lutando contra os mais habilidosos assassinos e larápios do reino. Mas ela não diz sim apenas para matar, seu foco é obter sua liberdade de volta.\n\nSe derrotar os 23 assassinos, ladrões e soldados, será a campeã do rei e estará livre depois de servi-lo por alguns anos.\n\nEndovier é uma sentença de morte, e cada duelo em Adarlan será para viver ou morrer. Mas se o preço é ser livre, e ela está disposta a tudo.\n\nSeu nome é Celaena Sardothien. O príncipe herdeiro vai provocá-la, o capitão da guarda fará tudo para protegê-la. E uma princesa de terras distantes se tornará algo que Celaena jamais pensou ter novamente: uma amiga.\n\nMas algo maligno habita o castelo – e está ali para matar. Quando os demais competidores começam a morrer, um a um e de maneira terrível, Celaena se vê mais uma vez envolvida em uma batalha pela sobrevivência e inicia uma jornada desesperada para desvendar a origem daquele mal antes que ele destrua o mundo dela. E sua única chance de ser livre.",
        "format": BookFormat.PAPERBACK,
        "pages": 392,
        "publication_date": Date(date(2012, 8, 7)),
        "language": "Português",
        "original_title": Name("Throne of Glass"),
        "secondary_genre_ids": ["2", "3"],
        "trope_ids": ["1", "2"],
        "series_id": "1",
        "original_series_id": "2",
        "book_number": 1.0,
        "publisher": "Galera",
        "isbn10": Isbn("9897541772"),
        "isbn13": Isbn("9789897541773"),
        "asin": "9897541772",
    }
    base.update(overrides)

    return base


def test_valid_book_should_be_created():
    book_data = make_book_data()
    book = Book(**make_book_data())

    assert book.id == book_data["id"]
    assert book.title == book_data["title"].value
    assert book.author_ids == book_data["author_ids"]
    assert book.main_genre_id == book_data["main_genre_id"]
    assert book.cover == book_data["cover"]
    assert book.synopsis == book_data["synopsis"]
    assert book.format == book_data["format"]
    assert book.pages == book_data["pages"]
    assert book.publication_date == book_data["publication_date"]
    assert book.language == book_data["language"]
    assert book.original_title == book_data["original_title"]
    assert book.secondary_genre_ids == book_data["secondary_genre_ids"]
    assert book.trope_ids == book_data["trope_ids"]
    assert book.series_id == book_data["series_id"]
    assert book.original_series_id == book_data["original_series_id"]
    assert book.book_number == book_data["book_number"]
    assert book.publisher == book_data["publisher"]
    assert book.isbn10 == book_data["isbn10"].value
    assert book.isbn13 == book_data["isbn13"].value
    assert book.asin == book_data["asin"]
    assert book.is_deleted == False
    assert book.deleted_at is None


def test_valid_book_without_asin_should_be_created():
    book_data = make_book_data(asin=None)
    book = Book(**book_data)


def test_valid_book_without_isbn_should_be_created():
    book_data = make_book_data(isbn13=None)
    book = Book(**book_data)


def test_valid_book_without_publisher_should_be_created():
    book_data = make_book_data(publisher=None)
    book = Book(**book_data)


def test_valid_book_without_book_number_should_be_created():
    book_data = make_book_data(book_number=None)
    book = Book(**book_data)


def test_valid_book_without_original_series_id_should_be_created():
    book_data = make_book_data(original_series_id=None)
    book = Book(**book_data)


def test_valid_book_without_series_id_should_be_created():
    book_data = make_book_data(series_id=None)
    book = Book(**book_data)


def test_invalid_title_should_raise_invalid_book_exception():
    book_data = make_book_data(title="")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_original_title_should_raise_invalid_book_exception():
    book_data = make_book_data(original_title="")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_author_ids_should_raise_invalid_book_exception():
    book_data = make_book_data(author_ids=[])

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_main_genre_should_raise_invalid_book_exception():
    book_data = make_book_data(main_genre_id="")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_secondary_genre_ids_should_raise_invalid_book_exception():
    book_data = make_book_data(secondary_genre_ids="")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_trope_ids_should_raise_invalid_book_exception():
    book_data = make_book_data(trope_ids="")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_cover_should_raise_invalid_book_exception():
    book_data = make_book_data(cover="")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_series_id_should_raise_invalid_book_exception():
    book_data = make_book_data(series_id=2)

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_original_series_id_should_raise_invalid_book_exception():
    book_data = make_book_data(original_series_id=2)

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_synopsis_should_raise_invalid_book_exception():
    book_data = make_book_data(synopsis="")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_format_should_raise_invalid_book_exception():
    book_data = make_book_data(format="paperback")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_pages_should_raise_invalid_book_exception():
    book_data = make_book_data(pages="320")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_book_number_should_raise_invalid_book_exception():
    book_data = make_book_data(book_number=2)

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_publication_date_should_raise_invalid_book_exception():
    book_data = make_book_data(publication_date="2025-01-01")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_publisher_should_raise_invalid_book_exception():
    book_data = make_book_data(publisher="")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_isbn13_should_raise_invalid_book_exception():
    book_data = make_book_data(isbn13="9789897541773")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_isbn10_should_raise_invalid_book_exception():
    book_data = make_book_data(isbn10="9789897541773")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_asin_should_raise_invalid_book_exception():
    book_data = make_book_data(asin="9789897541773")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_invalid_language_should_raise_invalid_book_exception():
    book_data = make_book_data(language="")

    with pytest.raises(InvalidBookException):
        Book(**book_data)


def test_soft_delete_marks_book_as_deleted():
    book = Book(**make_book_data())
    book.soft_delete()

    assert book.is_deleted is True
    assert book.deleted_at is not None
