from beanie import Document
from pydantic import Field, EmailStr
from datetime import datetime, date

from bookland.infra.mongo_models.utils import generate_uuid
from bookland.domain.enums import UserGender, UserRole
from bookland.infra.utils.dates_utils import datetime_now


class UserDocument(Document):
    id: str = Field(default_factory=generate_uuid, alias="_id")  # type: ignore[assignment]

    name: str
    nickname: str
    email: EmailStr
    password: str
    gender: UserGender | None = None
    birthdate: date | None = None
    ratings_count: int
    average_rating: float
    reviews_count: int
    avatar_url: str | None = None
    role: UserRole

    created_at: datetime = Field(default_factory=datetime_now)
    updated_at: datetime = Field(default_factory=datetime_now)

    class Settings:
        name = "users"
