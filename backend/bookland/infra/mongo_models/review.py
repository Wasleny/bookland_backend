from beanie import Document
from pydantic import Field, BaseModel
from datetime import datetime, date

from bookland.infra.mongo_models.utils import generate_uuid
from bookland.infra.utils.dates_utils import datetime_now


class ReadingCriteriaModel(BaseModel):
    criterion: str
    rating: int


class ReviewDocument(Document):
    id: str = Field(default_factory=generate_uuid, alias="_id")  # type: ignore[assignment]

    user_id: str
    book_id: str
    rating: int
    body: str
    spoiler: bool
    start_date: date
    end_date: date
    most_recent_reading: bool
    rating_composition_criteria: list[ReadingCriteriaModel]
    independent_rating_criteria: list[ReadingCriteriaModel]

    created_at: datetime = Field(default_factory=datetime_now)
    updated_at: datetime = Field(default_factory=datetime_now)

    class Settings:
        name = "reviews"
