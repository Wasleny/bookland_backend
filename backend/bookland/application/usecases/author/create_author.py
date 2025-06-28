from bookland.domain.entities.author import Author
from bookland.domain.repositories.author_repository import AuthorRepository


class CreateAuthorUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    async def execute(self, author: Author) -> Author:
        return await self._repository.create(author)
