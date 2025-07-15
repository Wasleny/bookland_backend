from bookland.domain.entities import Author
from bookland.domain.repositories import AuthorRepository


class GetAuthorByIdUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    async def execute(self, author_id: str) -> Author | None:
        return await self._repository.get_by_id(author_id)
