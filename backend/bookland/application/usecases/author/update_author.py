from bookland.domain.entities.author import Author
from bookland.domain.repositories.author_repository import AuthorRepository


class UpdateAuthorUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    async def execute(self, author: Author) -> Author | None:
        return await self._repository.update(author)
