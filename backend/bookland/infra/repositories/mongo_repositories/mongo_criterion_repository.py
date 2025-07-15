from bookland.domain.repositories import CriterionRepository
from bookland.domain.entities import Criterion
from bookland.domain.exceptions import CriterionNotFoundException

from bookland.infra.mappers import CriterionMapper
from bookland.infra.mongo_models import CriterionDocument
from bookland.infra.utils.dates_utils import datetime_now
from beanie.operators import Set


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
        criterion_to_update = CriterionMapper.to_document(criterion).model_dump(
            exclude_none=True, exclude={"id", "_id", "created_at", "deleted_at"}
        )

        filter = {"_id": criterion.id, "deleted_at": None}

        update_result = await CriterionDocument.find_one(filter).update(
            Set(criterion_to_update | {"updated_at": datetime_now()})
        )

        updated_criterion = await CriterionDocument.get(criterion.id)

        if updated_criterion is None or updated_criterion.deleted_at is not None:
            raise CriterionNotFoundException()

        return CriterionMapper.to_domain(updated_criterion)

    async def soft_delete(self, criterion_id: str) -> Criterion | None:
        criterion = await CriterionDocument.get(criterion_id)

        if criterion is None or criterion.deleted_at is not None:
            raise CriterionNotFoundException

        criterion.deleted_at = datetime_now()
        await criterion.save()

        return CriterionMapper.to_domain(criterion)

    async def search(self, search_term: str, user_id: str) -> list[Criterion]:
        documents = await CriterionDocument.find(
            {
                "name": {"$regex": search_term, "$options": "i"},
                "user_id": user_id,
                "deleted_at": None,
            }
        ).to_list()

        return [CriterionMapper.to_domain(doc) for doc in documents]
