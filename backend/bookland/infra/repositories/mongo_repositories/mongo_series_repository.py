from bookland.domain.entities import Series
from bookland.domain.repositories import SeriesRepository
from bookland.domain.exceptions import SeriesNotFoundException

from bookland.infra.mongo_models import SeriesDocument
from bookland.infra.mappers import SeriesMapper
from beanie.operators import Set
from bookland.infra.utils.dates_utils import datetime_now


class MongoSeriesRepository(SeriesRepository):
    async def get_all(self) -> list[Series]:
        documents = await SeriesDocument.find({"deleted_at": None}).to_list()

        return [SeriesMapper.to_domain(doc) for doc in documents]

    async def get_by_id(self, series_id: str) -> Series | None:
        document = await SeriesDocument.find_one({"_id": series_id, "deleted_at": None})

        if document:
            return SeriesMapper.to_domain(document)

        return None

    async def create(self, series: Series) -> Series:
        document = SeriesMapper.to_document(series)
        await document.insert()

        return SeriesMapper.to_domain(document)

    async def update(self, series: Series) -> Series:
        series_to_update = SeriesMapper.to_document(series).model_dump(
            exclude_none=True, exclude={"id", "_id", "created_at", "deleted_at"}
        )

        filter = {"_id": series.id, "deleted_at": None}

        update_result = await SeriesDocument.find_one(filter).update(
            Set(series_to_update | {"updated_at": datetime_now()})
        )

        if update_result.modified_count == 0:
            raise SeriesNotFoundException()

        updated_series = await SeriesDocument.get(series.id)

        if updated_series is None or updated_series.deleted_at is not None:
            raise SeriesNotFoundException()

        return SeriesMapper.to_domain(updated_series)

    async def soft_delete(self, series_id: str) -> Series | None:
        series = await SeriesDocument.get(series_id)

        if series is None or series.deleted_at is not None:
            raise SeriesNotFoundException

        series.deleted_at = datetime_now()
        await series.save()

        return SeriesMapper.to_domain(series)
