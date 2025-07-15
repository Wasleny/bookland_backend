from bookland.domain.entities import Bookshelf
from bookland.domain.repositories import BookshelfRepository

from bookland.infra.mongo_models import BookshelfDocument
from bookland.infra.mappers import BookshelfMapper


class MongoBookshelfRepository(BookshelfRepository):
    async def get_all(self) -> list[Bookshelf]:
        documents = await BookshelfDocument.find().to_list()

        return [BookshelfMapper.to_domain(doc) for doc in documents]
