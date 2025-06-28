from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from bookland.infra.mongo_models.author import AuthorDocument
from bookland.infra.mongo_models.user import UserDocument
from bookland.infra.settings import MONGO_URI


async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.bookland
    await init_beanie(database=db, document_models=[AuthorDocument, UserDocument])
