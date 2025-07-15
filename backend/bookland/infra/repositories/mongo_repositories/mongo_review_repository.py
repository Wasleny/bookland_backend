from bookland.domain.entities import Review
from bookland.domain.repositories import ReviewRepository
from bookland.domain.exceptions import ReviewNotFoundException

from bookland.infra.mongo_models import ReviewDocument
from bookland.infra.mappers import ReviewMapper
from bookland.infra.utils.dates_utils import datetime_now
from beanie.operators import Set


class MongoReviewRepository(ReviewRepository):
    async def get_by_id(self, review_id: str) -> Review | None:
        document = await ReviewDocument.find_one({"_id": review_id})

        if document:
            return ReviewMapper.to_domain(document)

        return None

    async def get_by_book(self, book_id: str) -> list[Review]:
        documents = await ReviewDocument.find({"book_id": book_id}).to_list()

        return [ReviewMapper.to_domain(doc) for doc in documents]

    async def get_by_user_and_book(self, user_id: str, book_id: str) -> list[Review]:
        documents = await ReviewDocument.find(
            {"book_id": book_id, "user_id": user_id}
        ).to_list()

        return [ReviewMapper.to_domain(doc) for doc in documents]

    async def get_book_most_recent_reading(
        self, user_id: str, book_id: str
    ) -> Review | None:
        document = await ReviewDocument.find_one(
            {"user_id": user_id, "book_id": book_id, "most_recent_reading": True}
        )

        if document:
            return ReviewMapper.to_domain(document)

        return None

    async def create(self, review: Review) -> Review:
        document = ReviewMapper.to_document(review)
        await document.insert()

        return ReviewMapper.to_domain(document)

    async def update(self, review: Review) -> Review | None:
        review_to_update = ReviewMapper.to_document(review).model_dump(
            exclude_none=True, exclude={"id", "_id", "created_at"}
        )

        filter = {"_id": review.id}

        update_result = await ReviewDocument.find_one(filter).update(
            Set(review_to_update | {"updated_at": datetime_now()})
        )

        if update_result.modified_count == 0:
            raise ReviewNotFoundException()

        updated_review = await ReviewDocument.get(review.id)

        if updated_review is None:
            raise ReviewNotFoundException()

        return ReviewMapper.to_domain(updated_review)

    async def delete(self, review_id: str) -> Review | None:
        document = await ReviewDocument.get(review_id)

        if not document:
            raise ReviewNotFoundException()

        await document.delete()

        return ReviewMapper.to_domain(document)

    async def delete_all_for_user_and_book(
        self, user_id: str, book_id: str
    ) -> list[Review]:
        documents = await ReviewDocument.find(
            {"user_id": user_id, "book_id": book_id}
        ).to_list()

        if not documents:
            return []

        for doc in documents:
            await doc.delete()

        return [ReviewMapper.to_domain(doc) for doc in documents]
