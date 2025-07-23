from bookland.domain.repositories import TropeRepository
from bookland.domain.entities import Trope

from bookland.infra.mappers import TropeMapper
from bookland.infra.mongo_models import TropeDocument


class MongoTropeRepository(TropeRepository):
    async def get_all(self) -> list[Trope]:
        documents = await TropeDocument.find({"deleted_at": None}).to_list()

        return [TropeMapper.to_domain(doc) for doc in documents]

    async def get_many_by_id(self, tropes_id) -> list[Trope]:
        documents = await TropeDocument.find_many({"_id": {"$in": tropes_id}}).to_list()

        return [TropeMapper.to_domain(doc) for doc in documents]
