from bookland.domain.repositories import CriterionRepository
from bookland.domain.entities.criterion import Criterion
from bookland.infra.mappers.criterion_mapper import CriterionMapper
from bookland.infra.mongo_models.criterion import CriterionDocument
from bookland.infra.utils.dates_utils import datetime_now


class MongoCriterionRepository(CriterionRepository):
    async def get_all(self, user_id: str) -> list[Criterion]:
        documents = await CriterionDocument.find(
            {"user_id": user_id, "deleted_at": None}
        ).to_list()

        return [CriterionMapper.to_domain(doc) for doc in documents]

    async def get_by_id(self, criterion_id: str) -> Criterion | None:
        document = await CriterionDocument.find_one(
            {"_id": criterion_id, "deleted_at": None}
        )

        if document:
            return CriterionMapper.to_domain(document)

        return None

    async def create(self, criterion: Criterion) -> Criterion:
        document = CriterionMapper.to_document(criterion)
        await document.insert()

        return CriterionMapper.to_domain(document)

    async def update(self, criterion: Criterion) -> Criterion | None:
        document = await CriterionDocument.find_one(
            {"_id": criterion.id, "deleted_at": None}
        )

        if not document:
            raise Exception("Critério não encontrado.")

        document.name = criterion.name.value
        document.description = criterion.description
        document.updated_at = datetime_now()

        await document.save()

        return CriterionMapper.to_domain(document)

    async def soft_delete(self, criterion_id: str) -> None:
        document = await CriterionDocument.get(criterion_id)

        if document:
            document.deleted_at = datetime_now()
            await document.save()

    async def search(self, search_term: str, user_id: str) -> list[Criterion]:
        documents = await CriterionDocument.find(
            {
                "name": {"$regex": search_term, "$options": "i"},
                "user_id": user_id,
                "deleted_at": None,
            }
        ).to_list()

        return [CriterionMapper.to_domain(doc) for doc in documents]
