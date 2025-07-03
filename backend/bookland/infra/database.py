from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from bookland.infra.mongo_models import (
    AuthorDocument,
    UserDocument,
    CriterionDocument,
    GenreDocument,
    TropeDocument,
)
from bookland.infra.settings import MONGO_URI


async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.bookland
    await init_beanie(
        database=db,
        document_models=[
            AuthorDocument,
            UserDocument,
            CriterionDocument,
            GenreDocument,
            TropeDocument,
        ],
    )
