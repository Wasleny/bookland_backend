from bookland.domain.entities.author import Author
from bookland.domain.repositories.author_repository import AuthorRepository


class GetAllAuthorsUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    async def execute(self) -> list[Author]:
        return await self._repository.get_all()
