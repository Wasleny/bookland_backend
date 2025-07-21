import os
import pytest_asyncio
import asyncio
from unittest.mock import AsyncMock, patch
from httpx import AsyncClient, ASGITransport
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from asgi_lifespan import LifespanManager

TEST_MONGO_URI = os.getenv(
    "TEST_MONGO_URI",
    "mongodb://root:rootpassword@mongo-test:27017/bookland_test?authSource=admin",
)

os.environ["MONGO_URI"] = TEST_MONGO_URI

from bookland.interfaces.api.main import app
from bookland.interfaces.api import deps
from bookland.infra import database
from bookland.infra.mongo_models import (
    AuthorDocument,
    BookDocument,
    BookshelfDocument,
    CriterionDocument,
    GenreDocument,
    ReadingInProgressDocument,
    ReviewDocument,
    SeriesDocument,
    TropeDocument,
    UserBookDocument,
    UserDocument,
)


@pytest_asyncio.fixture(scope="session")
def event_loop():
    """Evita conflitos de loop no pytest-asyncio."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def mongo_db():
    """Inicializa o banco e o Beanie com documentos, limpa antes e depois."""

    client = AsyncIOMotorClient(TEST_MONGO_URI)
    db = client.get_default_database()

    collections = [
        AuthorDocument,
        BookDocument,
        BookshelfDocument,
        CriterionDocument,
        GenreDocument,
        ReadingInProgressDocument,
        ReviewDocument,
        SeriesDocument,
        TropeDocument,
        UserBookDocument,
        UserDocument,
    ]

    await init_beanie(database=db, document_models=collections)

    for doc in collections:
        await doc.delete_all()

    yield db

    for doc in collections:
        await doc.delete_all()


@pytest_asyncio.fixture
async def client(mongo_db):
    """Cliente HTTP com override da dependência get_user_repository e patch em init_db."""

    async def fake_init_db():
        pass

    with patch.object(database, "init_db", new=fake_init_db):

        async def override_get_user_repository():
            from bookland.infra.repositories import MongoUserRepository
            return MongoUserRepository()

        app.dependency_overrides[deps.get_user_repository] = override_get_user_repository

        async with LifespanManager(app):
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as ac:
                yield ac

        app.dependency_overrides.clear()
