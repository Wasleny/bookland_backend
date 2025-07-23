from bookland.domain.entities import Author
from bookland.domain.repositories import AuthorRepository


class GetManyAuthorsByIdUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    async def execute(self, author_ids: list[str]) -> list[Author]:
        return await self._repository.get_many_by_id(author_ids)
