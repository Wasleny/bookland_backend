from bookland.domain.entities import Author
from bookland.domain.repositories import AuthorRepository
from bookland.domain.exceptions import AuthorNotFoundException

from bookland.infra.mongo_models import AuthorDocument
from bookland.infra.mappers import AuthorMapper
from bookland.infra.utils.dates_utils import datetime_now
from beanie.operators import Set


class MongoAuthorRepository(AuthorRepository):
    async def get_all(self) -> list[Author]:
        documents = await AuthorDocument.find({"deleted_at": None}).to_list()

        return [AuthorMapper.to_domain(doc) for doc in documents]

    async def get_by_id(self, author_id: str) -> Author | None:
        document = await AuthorDocument.find_one({"_id": author_id, "deleted_at": None})

        if document:
            return AuthorMapper.to_domain(document)

        return None

    async def create(self, author: Author) -> Author:
        document = AuthorMapper.to_document(author)
        await document.insert()

        return AuthorMapper.to_domain(document)

    async def update(self, author: Author) -> Author | None:
        author_to_update = AuthorMapper.to_document(author).model_dump(
            exclude_none=True, exclude={"id", "_id", "created_at", "deleted_at"}
        )

        filter = {"_id": author.id, "deleted_at": None}

        update_result = await AuthorDocument.find_one(filter).update(
            Set(author_to_update | {"updated_at": datetime_now()})
        )

        if update_result.modified_count == 0:
            raise AuthorNotFoundException()

        updated_author = await AuthorDocument.get(author.id)

        if updated_author is None or updated_author.deleted_at is not None:
            raise AuthorNotFoundException()

        return AuthorMapper.to_domain(updated_author)

    async def soft_delete(self, author_id: str) -> Author | None:
        author = await AuthorDocument.get(author_id)

        if author is None or author.deleted_at is not None:
            raise AuthorNotFoundException

        author.deleted_at = datetime_now()
        await author.save()

        return AuthorMapper.to_domain(author)
