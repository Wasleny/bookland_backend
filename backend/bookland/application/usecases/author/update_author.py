from bookland.domain.entities import Author
from bookland.domain.repositories import AuthorRepository


class UpdateAuthorUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    async def execute(self, author: Author) -> Author | None:
        return await self._repository.update(author)
