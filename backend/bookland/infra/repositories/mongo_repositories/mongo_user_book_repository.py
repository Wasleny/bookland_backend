from bookland.domain.repositories import UserBookRepository
from bookland.domain.exceptions import UserBookNotFoundException
from bookland.domain.entities import UserBook

from bookland.infra.mongo_models import UserBookDocument
from bookland.infra.mappers import UserBookMapper
from beanie.operators import Set
from bookland.infra.utils.dates_utils import datetime_now


class MongoUserBookRepository(UserBookRepository):
    async def get_by_user(self, user_id: str) -> list[UserBook]:
        documents = await UserBookDocument.find({"user_id": user_id}).to_list()

        return [UserBookMapper.to_domain(doc) for doc in documents]

    async def get_by_user_and_book(self, user_id: str, book_id: str) -> UserBook | None:
        document = await UserBookDocument.find_one(
            {"user_id": user_id, "book_id": book_id}
        )

        if document:
            return UserBookMapper.to_domain(document)

        return None

    async def create(self, user_book: UserBook) -> UserBook:
        document = UserBookMapper.to_document(user_book)
        await document.insert()

        return UserBookMapper.to_domain(document)

    async def update(self, user_book: UserBook) -> UserBook | None:
        user_book_to_update = UserBookMapper.to_document(user_book).model_dump(
            exclude_none=True, exclude={"id", "_id", "created_at", "deleted_at"}
        )

        filter = {"_id": user_book.id, "deleted_at": None}

        update_result = await UserBookDocument.find_one(filter).update(
            Set(user_book_to_update | {"updated_at": datetime_now()})
        )

        if update_result.modified_count == 0:
            raise UserBookNotFoundException()

        updated_user_book = await UserBookDocument.get(user_book.id)

        if updated_user_book is None or updated_user_book.deleted_at is not None:
            raise UserBookNotFoundException()

        return UserBookMapper.to_domain(updated_user_book)

    async def delete(self, user_book_id: str) -> UserBook | None:
        document = await UserBookDocument.get(user_book_id)

        if not document:
            raise UserBookNotFoundException()

        await document.delete()

        return UserBookMapper.to_domain(document)

    async def get_by_id(self, user_book_id: str) -> UserBook | None:
        document = await UserBookDocument.find_one({"_id": user_book_id})

        if document:
            return UserBookMapper.to_domain(document)

        return None
