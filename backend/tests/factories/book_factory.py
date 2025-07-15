import pytest
from uuid import uuid4
from datetime import date

from bookland.domain.entities import Book
from bookland.domain.value_objects import Title, Isbn, Date, Slug
from bookland.domain.enums import BookFormat


def create_book(**overrides):
    base = {
        "id": str(uuid4()),
        "title": Title("Trono de Vidro"),
        "author_ids": ["1"],
        "main_genre_id": "1",
        "cover": "path/to/image",
        "synopsis": "A magia há muito abandonou Adarlan. Um perverso rei governa, punindo impiedosamente as minorias rebeldes.\n\nAos 18 anos uma prisioneira está cumprindo sua sentença. Ela é uma assassina, e a melhor de Adarlan. Aprisionada e fraca, ela está quase perdendo as esperanças, a sentença de morte é iminente, mas a jovem recebe uma proposta inesperada: representar o príncipe em uma competição com lutando contra os mais habilidosos assassinos e larápios do reino. Mas ela não diz sim apenas para matar, seu foco é obter sua liberdade de volta.\n\nSe derrotar os 23 assassinos, ladrões e soldados, será a campeã do rei e estará livre depois de servi-lo por alguns anos.\n\nEndovier é uma sentença de morte, e cada duelo em Adarlan será para viver ou morrer. Mas se o preço é ser livre, e ela está disposta a tudo.\n\nSeu nome é Celaena Sardothien. O príncipe herdeiro vai provocá-la, o capitão da guarda fará tudo para protegê-la. E uma princesa de terras distantes se tornará algo que Celaena jamais pensou ter novamente: uma amiga.\n\nMas algo maligno habita o castelo – e está ali para matar. Quando os demais competidores começam a morrer, um a um e de maneira terrível, Celaena se vê mais uma vez envolvida em uma batalha pela sobrevivência e inicia uma jornada desesperada para desvendar a origem daquele mal antes que ele destrua o mundo dela. E sua única chance de ser livre.",
        "format": BookFormat.PAPERBACK,
        "pages": 392,
        "publication_date": Date(date(2012, 8, 7)),
        "language": "Português",
        "original_title": Title("Throne of Glass"),
        "slug": Slug("trono-de-vidro"),
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

    return Book(**base)
