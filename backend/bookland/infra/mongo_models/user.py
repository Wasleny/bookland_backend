from beanie import Document
from pydantic import Field, EmailStr
from datetime import datetime, date

from bookland.infra.mongo_models.utils import generate_uuid, utc_now
from bookland.domain.enums.user_gender import UserGender
from bookland.domain.enums.user_role import UserRole


class UserDocument(Document):
    id: str = Field(default_factory=generate_uuid, alias="_id")
    name: str
    nickname: str
    email: EmailStr
    password: str
    gender: UserGender | None = None
    birthday: date | None = None
    avatar_url: str | None = None
    role: UserRole
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    deleted_at: datetime | None = None

    class Settings:
        name = "users"
