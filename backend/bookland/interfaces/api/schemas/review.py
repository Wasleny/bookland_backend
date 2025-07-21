from pydantic import BaseModel, Field


class ReviewSchema(BaseModel):
    book_id: str = Field(..., description="ID do livro")
    spoiler: str = Field(..., description="Indica se a resenha contém spoilers")
    rating: str = Field(..., description="Nota atribuída à leitura")
    body: str = Field(
        ..., min_length=5, max_length=5000, description="Corpo da resenha"
    )
    start_date: str | None = Field(
        ...,
        description="Data de início da leitura (formato YYYY-MM-DD)",
    )
    end_date: str | None = Field(
        ...,
        description="Data de finalização da leitura (formato YYYY-MM-DD)",
    )
    rating_composition_criteria: list[dict] = Field(
        ..., description="Critérios de composição da nota"
    )
    independent_rating_criteria: list[dict] = Field(
        ..., description="Critérios independentes avaliados na leitura"
    )


class CreateReviewSchema(ReviewSchema): ...


class UpdateReviewSchema(ReviewSchema): ...


class PersonalReviewResponseSchema(BaseModel):
    id: str = Field(..., description="ID da resenha")
    user_id: str = Field(..., description="ID do usuário")
    book: dict = Field(..., description="Livro relacionado à resenha")
    spoiler: bool = Field(..., description="Indica se a resenha contém spoilers")
    most_recent_reading: bool = Field(
        ..., description="Indica se é a leitura mais recente do livro"
    )
    rating: int = Field(..., description="Nota atribuída à leitura")
    body: str = Field(..., description="Corpo da resenha")
    start_date: str | None = Field(
        ..., description="Data de início da leitura (formato YYYY-MM-DD)"
    )
    end_date: str | None = Field(
        ..., description="Data de finalização da leitura (formato YYYY-MM-DD)"
    )
    rating_composition_criteria: list[dict] = Field(
        ..., description="Critérios de composição da nota"
    )
    independent_rating_criteria: list[dict] = Field(
        ..., description="Critérios independentes avaliados na leitura"
    )

    @classmethod
    def from_entity(cls, review):
        return cls(
            id=review.id,
            user_id=review.user_id,
            book={
                "id": review.book.id,
                "title": review.book.title,
                "authors": review.book.authors,
            },
            spoiler=review.spoiler,
            most_recent_reading=review.most_recent_reading,
            rating=review.rating.value if review.rating else None,
            body=review.body,
            start_date=review.start_date.to_json() if review.start_date else None,
            end_date=review.end_date.to_json() if review.end_date else None,
            rating_composition_criteria=[
                criterion.to_dict() for criterion in review.rating_composition_criteria
            ],
            independent_rating_criteria=[
                criterion.to_dict() for criterion in review.independent_rating_criteria
            ],
        )


class PublicReviewResponseSchema(BaseModel):
    id: str = Field(..., description="ID da resenha")
    book_id: str = Field(..., description="ID do livro")
    user: dict = Field(..., description="Usuário relacionado à resenha")
    spoiler: bool = Field(..., description="Indica se a resenha contém spoilers")
    rating: int = Field(..., description="Nota atribuída à leitura")
    body: str = Field(..., description="Corpo da resenha")
    start_date: str | None = Field(
        ..., description="Data de início da leitura (formato YYYY-MM-DD)"
    )
    end_date: str | None = Field(
        ..., description="Data de finalização da leitura (formato YYYY-MM-DD)"
    )

    @classmethod
    def from_entity(cls, review):
        return cls(
            id=review.id,
            book_id=review.book_id,
            user={
                "id": review.user.id,
                "average_rating": review.user.average_rating.value,
                "reviews_count": review.user.reviews_count,
                "ratings_count": review.user.ratings_count,
            },
            spoiler=review.spoiler,
            rating=review.rating.value if review.rating else None,
            body=review.body,
            start_date=review.start_date.to_json() if review.start_date else None,
            end_date=review.end_date.to_json() if review.end_date else None,
        )
