from bookland.domain.repositories import GenreRepository
from bookland.domain.entities import Genre

from bookland.infra.mappers import GenreMapper
from bookland.infra.mongo_models import GenreDocument


class MongoGenreRepository(GenreRepository):
    async def get_all(self) -> list[Genre]:
        documents = await GenreDocument.find({"deleted_at": None}).to_list()

        return [GenreMapper.to_domain(doc) for doc in documents]
