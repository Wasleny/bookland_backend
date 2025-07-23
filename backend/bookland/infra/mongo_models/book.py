from beanie import Document
from pydantic import Field, constr
from datetime import datetime, date

from bookland.infra.mongo_models.utils import generate_uuid
from bookland.infra.utils.dates_utils import datetime_now


class BookDocument(Document):
    id: str = Field(default_factory=generate_uuid, alias="_id")  # type: ignore[assignment]

    title: str
    original_title: str
    author_ids: list[str]
    main_genre_id: str
    secondary_genre_ids: list[str]
    trope_ids: list[str]
    cover: str
    series_id: str | None
    original_series_id: str | None
    book_number: float | None
    average_rating: float
    reviews_count: int
    ratings_count: int
    synopsis: str
    format: str
    pages: int
    publication_date: date
    publisher: str | None
    isbn10: str | None
    isbn13: str | None
    asin: str | None
    language: str
    alternative_edition_ids: list[str]
    slug: str

    created_at: datetime = Field(default_factory=datetime_now)
    updated_at: datetime = Field(default_factory=datetime_now)
    deleted_at: datetime | None = None

    class Settings:
        name = "books"
