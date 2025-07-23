from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=150, description="Título do livro")
    original_title: str = Field(
        ..., min_length=1, max_length=150, description="Título original do livro"
    )
    author_ids: list = Field(..., description="Lista de IDs dos autores do livro")
    main_genre_id: str = Field(..., description="ID do gênero principal do livro")
    secondary_genre_ids: list = Field(
        ..., description="Lista de IDs dos gêneros secundários do livro"
    )
    trope_ids: list = Field(..., description="Lista de IDs das tropes do livro")
    cover: str = Field(..., description="URL da capa do livro")
    series_id: str | None = Field(..., description="ID da série do livro")
    original_series_id: str | None = Field(
        ..., description="ID da série original do livro"
    )
    book_number: float | None = Field(
        ..., description="Volume dentro da série do livro"
    )
    average_rating: float | None = Field(..., description="Avaliação média do livro")
    reviews_count: float | None = Field(..., description="Total de resenhas do livro")
    ratings_count: float | None = Field(..., description="Total de avaliações do livro")
    synopsis: str = Field(..., description="Sinopse do livro")
    format: str = Field(..., description="Formato do livro")
    pages: int = Field(..., description="Quantidade de páginas do livro")
    publication_date: str = Field(..., description="Data de publicação do livro")
    publisher: str = Field(..., description="Editora que publicou a obra")
    isbn10: str | None = Field(
        ..., min_length=10, max_length=10, description="ISBN-10 do livro"
    )
    isbn13: str | None = Field(
        ..., min_length=13, max_length=13, description="ISBN-13 do livro"
    )
    asin: str | None = Field(
        ..., min_length=10, max_length=10, description="ASIN do livro"
    )
    language: str = Field(..., description="Idioma do livro")
    alternative_edition_ids: list | None = Field(
        ..., description="Lista de IDs das obras alternativas (outras edições)"
    )
    slug: str = Field(
        ..., min_length=3, max_length=30, description="Slug do título do livro"
    )


class CreateBookSchema(BookSchema): ...


class UpdateBookSchema(BookSchema): ...


class BookDataSchema(BaseModel):
    id: str = Field(..., description="ID do livro")
    title: str = Field(..., description="Título do livro")
    original_title: str = Field(..., description="Título original do livro")
    authors: list = Field(..., description="Lista dos autores do livro")
    main_genre: dict = Field(..., description="Gênero principal do livro")
    secondary_genres: list = Field(
        ..., description="Lista dos gêneros secundários do livro"
    )
    tropes: list = Field(..., description="Lista das tropes do livro")
    cover: str = Field(..., description="URL da capa do livro")
    series: str | None = Field(..., description="Série do livro")
    original_series: str | None = Field(..., description="Série original do livro")
    book_number: float | None = Field(
        ..., description="Volume dentro da série do livro"
    )
    average_rating: float = Field(..., description="Avaliação média do livro")
    reviews_count: float = Field(..., description="Total de resenhas do livro")
    ratings_count: float = Field(..., description="Total de avaliações do livro")
    synopsis: str = Field(..., description="Sinopse do livro")
    format: str = Field(..., description="Formato do livro")
    pages: int = Field(..., description="Quantidade de páginas do livro")
    publication_date: str = Field(..., description="Data de publicação do livro")
    publisher: str = Field(..., description="Editora que publicou a obra")
    isbn10: str | None = Field(..., description="ISBN-10 do livro")
    isbn13: str | None = Field(..., description="ISBN-13 do livro")
    asin: str | None = Field(..., description="ASIN do livro")
    language: str = Field(..., description="Idioma do livro")
    alternative_edition_ids: list | None = Field(
        ..., description="Lista de IDs das obras alternativas (outras edições)"
    )
    slug: str = Field(..., description="Slug do título do livro")

    @classmethod
    def model_validate(cls, book):
        return cls(
            id=book["id"],
            title=book["title"],
            original_title=book["original_title"],
            authors=[
                {
                    "id": author.id,
                    "name": author.name.value,
                }
                for author in book["authors"]
            ],
            main_genre={
                "id": book["main_genre"].id,
                "name": book["main_genre"].name.value,
            },
            secondary_genres=[
                {"id": genre.id, "name": genre.name.value}
                for genre in book["secondary_genres"]
            ],
            tropes=[
                {"id": trope.id, "name": trope.name.value} for trope in book["tropes"]
            ],
            cover=book["cover"],
            series=book["series"],
            original_series=book["original_series"],
            book_number=book["book_number"],
            average_rating=book["average_rating"],
            reviews_count=book["reviews_count"],
            ratings_count=book["ratings_count"],
            synopsis=book["synopsis"],
            format=book["format"],
            pages=book["pages"],
            publication_date=book["publication_date"],
            publisher=book["publisher"],
            isbn10=book["isbn10"] if book["isbn10"] else None,
            isbn13=book["isbn13"] if book["isbn13"] else None,
            asin=book["asin"],
            language=book["language"],
            alternative_edition_ids=book["alternative_edition_ids"],
            slug=book["slug"],
        )


class BookWithoutRelationsSchema(BaseModel):
    id: str = Field(..., description="ID do livro")
    title: str = Field(..., description="Título do livro")
    original_title: str = Field(..., description="Título original do livro")
    author_ids: list = Field(..., description="Lista dos IDs dos autores")
    main_genre_id: str = Field(..., description="ID do gênero principal do livro")
    secondary_genre_ids: list = Field(
        ..., description="Lista dos IDs dos gêneros secundários do livro"
    )
    trope_ids: list = Field(..., description="Lista dos IDs das tropes do livro")
    cover: str = Field(..., description="URL da capa do livro")
    series_id: str | None = Field(..., description="ID da série do livro")
    original_series_id: str | None = Field(
        ..., description="ID da série original do livro"
    )
    book_number: float | None = Field(
        ..., description="Volume dentro da série do livro"
    )
    average_rating: float = Field(..., description="Avaliação média do livro")
    reviews_count: float = Field(..., description="Total de resenhas do livro")
    ratings_count: float = Field(..., description="Total de avaliações do livro")
    synopsis: str = Field(..., description="Sinopse do livro")
    format: str = Field(..., description="Formato do livro")
    pages: int = Field(..., description="Quantidade de páginas do livro")
    publication_date: str = Field(..., description="Data de publicação do livro")
    publisher: str = Field(..., description="Editora que publicou a obra")
    isbn10: str | None = Field(..., description="ISBN-10 do livro")
    isbn13: str | None = Field(..., description="ISBN-13 do livro")
    asin: str | None = Field(..., description="ASIN do livro")
    language: str = Field(..., description="Idioma do livro")
    alternative_edition_ids: list | None = Field(
        ..., description="Lista de IDs das obras alternativas (outras edições)"
    )
    slug: str = Field(..., description="Slug do título do livro")

    @classmethod
    def from_entity(cls, book):
        return cls(
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
            publication_date=book.publication_date.to_json(),
            publisher=book.publisher,
            isbn10=book.isbn10.value if book.isbn10 else None,
            isbn13=book.isbn13.value if book.isbn13 else None,
            asin=book.asin,
            language=book.language,
            alternative_edition_ids=book.alternative_edition_ids,
            slug=book.slug.value,
        )


class AllBooksResponseSchema(BaseModel):
    message: str = Field(..., description="Mensagem")
    books: list[BookDataSchema] = Field(..., description="Lista de livros")

    @classmethod
    def from_entity(cls, books, message):
        return cls(
            message=message,
            books=books,
        )


class BookResponseSchema(BaseModel):
    message: str = Field(..., description="Mensagem")
    book: BookDataSchema = Field(..., description="Dados do livro")

    @classmethod
    def from_entity(cls, book, message):
        return cls(
            message=message,
            book=book,
        )
