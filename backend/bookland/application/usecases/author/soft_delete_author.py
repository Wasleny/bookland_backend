from bookland.domain.repositories import AuthorRepository
from bookland.domain.entities import Author


class SoftDeleteAuthorUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    async def execute(self, author_id: str) -> Author | None:
        return await self._repository.soft_delete(author_id)
