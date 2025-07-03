from dotenv import load_dotenv
from pathlib import Path
import os
from uuid import uuid4
import json

from bookland.interfaces.api.services import search_user_usecase, register_user_usecase
from bookland.domain.entities import User, Genre, Trope
from bookland.domain.value_objects import Name, Nickname, Password, Email, Label, Slug
from bookland.domain.enums import UserGender, UserRole
from bookland.interfaces.api.security import get_password_hash
from bookland.infra.mappers import GenreMapper, TropeMapper
from bookland.infra.mongo_models import GenreDocument, TropeDocument


env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

ADMIN_NAME = os.getenv("ADMIN_NAME", "Super Admin")
ADMIN_NICKNAME = os.getenv("ADMIN_NICKNAME", "super_admin")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@bookland.com")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "adminpass")


async def create_default_admin_user():
    existing_admin = await search_user_usecase.execute(ADMIN_EMAIL)

    if existing_admin is None:
        admin_user = User(
            id=str(uuid4()),
            name=Name(ADMIN_NAME),
            nickname=Nickname(ADMIN_NICKNAME),
            email=Email(ADMIN_EMAIL),
            password=Password(get_password_hash(ADMIN_PASSWORD)),
            gender=UserGender.UNSPECIFIED,
            birthday=None,
            avatar_url=None,
            role=UserRole.ADMIN,
        )

        await register_user_usecase.execute(admin_user)


async def populate_genres():
    path = Path(__file__).parent / "data" / "genres.json"
    with open(path, encoding="utf-8", mode="r") as f:
        genres = json.load(f)

    genre_documents = await GenreDocument.find().to_list()

    if len(genre_documents) == 0:
        for genre_data in genres:
            genre = Genre(
                str(uuid4()), Label(genre_data["name"]), Slug(genre_data["slug"])
            )
            document = GenreMapper.to_document(genre)
            await document.insert()


async def populate_tropes():
    path = Path(__file__).parent / "data" / "tropes.json"
    with open(path, encoding="utf-8", mode="r") as f:
        tropes = json.load(f)

    trope_documents = await TropeDocument.find().to_list()

    if len(trope_documents) == 0:
        for trope_data in tropes:
            trope = Trope(
                str(uuid4()), Label(trope_data["name"]), Slug(trope_data["slug"])
            )
            document = TropeMapper.to_document(trope)
            await document.insert()
