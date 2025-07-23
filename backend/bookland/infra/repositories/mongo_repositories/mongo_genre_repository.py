from bookland.domain.repositories import GenreRepository
from bookland.domain.entities import Genre

from bookland.infra.mappers import GenreMapper
from bookland.infra.mongo_models import GenreDocument


class MongoGenreRepository(GenreRepository):
    async def get_all(self) -> list[Genre]:
        documents = await GenreDocument.find({"deleted_at": None}).to_list()

        return [GenreMapper.to_domain(doc) for doc in documents]

    async def get_many_by_id(self, genre_ids) -> list[Genre]:
        if not genre_ids:
            return []

        documents = await GenreDocument.find_many({"_id": {"$in": genre_ids}}).to_list()

        return [GenreMapper.to_domain(doc) for doc in documents]

    async def get_by_id(self, genre_id) -> Genre | None:
        document = await GenreDocument.find_one({"_id": genre_id})

        if not document:
            return None

        return GenreMapper.to_domain(document)
