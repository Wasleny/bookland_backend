from beanie import Document
from pydantic import Field
from datetime import datetime

from bookland.infra.mongo_models.utils import generate_uuid, utc_now


class AuthorDocument(Document):
    id: str = Field(default_factory=generate_uuid, alias="_id")
    name: str
    nationality: str | None = None
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    deleted_at: datetime | None = None

    class Settings:
        name = "authors"
