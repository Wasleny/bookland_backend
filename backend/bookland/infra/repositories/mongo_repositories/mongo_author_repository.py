from bookland.infra.utils.dates_utils import datetime_now
from bookland.domain.entities.author import Author
from bookland.infra.mongo_models.author import AuthorDocument
from bookland.infra.mappers.author_mapper import AuthorMapper
from bookland.domain.repositories.author_repository import AuthorRepository


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

    async def update(self, author: Author) -> Author:
        document = await AuthorDocument.get(author.id)

        if not document:
            raise Exception("Autor não encontrado.")

        document.name = author.name.value
        document.nationality = author.nationality
        document.updated_at = datetime_now()

        await document.save()

        return AuthorMapper.to_domain(document)

    async def soft_delete(self, author_id: str) -> None:
        document = await AuthorDocument.get(author_id)

        if document:
            document.deleted_at = datetime_now()
            await document.save()
