from beanie.operators import Set
import re
from typing import Any

from bookland.domain.entities import Book
from bookland.domain.repositories import BookRepository
from bookland.domain.exceptions import BookNotFoundException

from bookland.infra.mongo_models import BookDocument
from bookland.infra.mappers import BookMapper
from bookland.infra.utils.dates_utils import datetime_now


class MongoBookRepository(BookRepository):
    async def create(self, book: Book) -> Book:
        document = BookMapper.to_document(book)
        await document.insert()
        return BookMapper.to_domain(document)

    async def get_by_id(self, book_id: str) -> Book | None:
        document = await BookDocument.find_one({"_id": book_id, "deleted_at": None})
        if document:
            return BookMapper.to_domain(document)
        return None

    async def get_all(self) -> list[Book]:
        documents = await BookDocument.find({"deleted_at": None}).to_list()
        return [BookMapper.to_domain(doc) for doc in documents]

    async def update(self, book: Book) -> Book | None:
        book_to_update = BookMapper.to_document(book).model_dump(
            exclude_none=True, exclude={"id", "_id", "created_at", "deleted_at"}
        )

        filter = {"_id": book.id, "deleted_at": None}

        update_result = await BookDocument.find_one(filter).update(
            Set(book_to_update | {"updated_at": datetime_now()})
        )

        if update_result.modified_count == 0:
            raise BookNotFoundException()

        updated_book = await BookDocument.get(book.id)

        if updated_book is None or updated_book.deleted_at is not None:
            raise BookNotFoundException()

        return BookMapper.to_domain(updated_book)

    async def soft_delete(self, book_id: str) -> Book | None:
        book = await BookDocument.get(book_id)

        if book is None or book.deleted_at is not None:
            raise BookNotFoundException

        book.deleted_at = datetime_now()
        await book.save()

        return BookMapper.to_domain(book)

    async def search(self, search_terms: dict[str, Any]) -> list[Book]:
        query = self.build_dynamic_query(BookDocument, search_terms)
        documents = await BookDocument.find(query).to_list()
        return [BookMapper.to_domain(doc) for doc in documents]

    @staticmethod
    def build_dynamic_query(model_cls, search_terms: dict[str, Any]) -> dict:
        conditions = []

        for field, value in search_terms.items():
            if value is None:
                continue

            if field not in model_cls.model_fields:
                continue

            if isinstance(value, str):
                regex = re.compile(re.escape(value), re.IGNORECASE)
                conditions.append({field: {"$regex": regex}})
            elif isinstance(value, list):
                conditions.append({field: {"$in": value}})  # type: ignore
            else:
                conditions.append({field: value})

        return {"$or": conditions} if conditions else {}
