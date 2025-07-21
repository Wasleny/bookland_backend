from uuid import uuid4
from pathlib import Path
import json
from datetime import date

from bookland.domain.entities import User, Genre, Trope, Bookshelf
from bookland.domain.value_objects import Name, Nickname, Password, Email, Label, Slug, BirthDate
from bookland.domain.enums import UserGender, UserRole
from bookland.interfaces.api.security import get_password_hash
from bookland.infra.mappers import GenreMapper, TropeMapper, BookshelfMapper, UserMapper
from bookland.infra.mongo_models import (
    GenreDocument,
    TropeDocument,
    BookshelfDocument,
    UserDocument,
)
from bookland.settings import ADMIN_NAME, ADMIN_NICKNAME, ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_AVATAR_URL


async def create_default_admin_user():
    existing_admin = await UserDocument.find_one({"email": ADMIN_EMAIL})

    if existing_admin is None:
        admin_user = User(
            id=str(uuid4()),
            name=Name(ADMIN_NAME),
            nickname=Nickname(ADMIN_NICKNAME),
            email=Email(ADMIN_EMAIL),
            password=Password(get_password_hash(ADMIN_PASSWORD)),
            gender=UserGender.UNSPECIFIED,
            birthdate=BirthDate(date(2002, 4, 29)),
            avatar_url=ADMIN_AVATAR_URL,
            role=UserRole.ADMIN,
        )

        document = UserMapper.to_document(admin_user)
        await document.insert()


async def populate_genres():
    path = Path(__file__).parent / "data" / "genres.json"
    with open(path, encoding="utf-8", mode="r") as f:
        genres = json.load(f)

    genre_documents = await GenreDocument.find().to_list()

    if len(genre_documents) == 0:
        for genre_data in genres:
            genre = Genre(
                str(uuid4()),
                Label(genre_data["name"]),
                Label(genre_data["name_pt_br"]),
                Slug(genre_data["slug"]),
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
                str(uuid4()),
                Label(trope_data["name"]),
                Label(trope_data["name_pt_br"]),
                Slug(trope_data["slug"]),
            )
            document = TropeMapper.to_document(trope)
            await document.insert()


async def populate_bookshelves():
    path = Path(__file__).parent / "data" / "shelves.json"
    with open(path, encoding="utf-8", mode="r") as f:
        shelves = json.load(f)

    shelf_documents = await BookshelfDocument.find().to_list()

    if len(shelf_documents) == 0:
        for shelf_data in shelves:
            shelf = Bookshelf(
                str(uuid4()), Label(shelf_data["name"]), Slug(shelf_data["slug"])
            )
            document = BookshelfMapper.to_document(shelf)
            await document.insert()
