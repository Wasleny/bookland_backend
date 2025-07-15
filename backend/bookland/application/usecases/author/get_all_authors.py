from bookland.domain.entities import Author
from bookland.domain.repositories import AuthorRepository


class GetAllAuthorsUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    async def execute(self) -> list[Author]:
        return await self._repository.get_all()
