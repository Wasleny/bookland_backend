from beanie import Document
from pydantic import Field
from datetime import datetime

from bookland.infra.mongo_models.utils import generate_uuid
from bookland.infra.utils.dates_utils import datetime_now


class UserBookDocument(Document):
    id: str = Field(default_factory=generate_uuid, alias="_id")  # type: ignore[assignment]

    book_id: str
    user_id: str
    default_bookshelf_id: str

    created_at: datetime = Field(default_factory=datetime_now)
    updated_at: datetime = Field(default_factory=datetime_now)

    class Settings:
        name = "users_books"
