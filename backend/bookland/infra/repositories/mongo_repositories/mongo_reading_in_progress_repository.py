from bookland.domain.entities import ReadingInProgress
from bookland.domain.repositories import ReadingInProgressRepository
from bookland.domain.exceptions import ReadingInProgressNotFoundException

from bookland.infra.mongo_models import ReadingInProgressDocument
from bookland.infra.mappers import ReadingInProgressMapper
from bookland.infra.utils.dates_utils import datetime_now
from beanie.operators import Set


class MongoReadingInProgressRepository(ReadingInProgressRepository):
    async def get_by_user(self, user_id: str) -> list[ReadingInProgress]:
        documents = await ReadingInProgressDocument.find({"user_id": user_id}).to_list()

        return [ReadingInProgressMapper.to_domain(doc) for doc in documents]

    async def get_by_user_and_book(
        self, user_id: str, book_id: str
    ) -> ReadingInProgress | None:
        document = await ReadingInProgressDocument.find_one(
            {"user_id": user_id, "book_id": book_id}
        )

        if document:
            return ReadingInProgressMapper.to_domain(document)

        return None

    async def get_by_id(self, reading_in_progress_id: str) -> ReadingInProgress | None:
        document = await ReadingInProgressDocument.find_one(
            {"_id": reading_in_progress_id}
        )

        if document:
            return ReadingInProgressMapper.to_domain(document)

        return None

    async def create(self, reading_in_progress: ReadingInProgress) -> ReadingInProgress:
        document = ReadingInProgressMapper.to_document(reading_in_progress)
        await document.insert()

        return ReadingInProgressMapper.to_domain(document)

    async def update(
        self, reading_in_progress: ReadingInProgress
    ) -> ReadingInProgress | None:
        reading_in_progress_to_update = ReadingInProgressMapper.to_document(
            reading_in_progress
        ).model_dump(exclude_none=True, exclude={"id", "_id", "created_at"})

        filter = {"_id": reading_in_progress.id}

        update_result = await ReadingInProgressDocument.find_one(filter).update(
            Set(reading_in_progress_to_update | {"updated_at": datetime_now()})
        )

        if update_result.modified_count == 0:
            raise ReadingInProgressNotFoundException()

        updated_reading_in_progress = await ReadingInProgressDocument.get(
            reading_in_progress.id
        )

        if updated_reading_in_progress is None:
            raise ReadingInProgressNotFoundException()

        return ReadingInProgressMapper.to_domain(updated_reading_in_progress)

    async def delete(self, reading_in_progress_id: str) -> ReadingInProgress | None:
        document = await ReadingInProgressDocument.get(reading_in_progress_id)

        if not document:
            raise ReadingInProgressNotFoundException()

        await document.delete()

        return ReadingInProgressMapper.to_domain(document)
