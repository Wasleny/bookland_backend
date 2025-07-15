from bookland.domain.repositories import GenreRepository
from bookland.domain.entities import Genre


class GetAllGenresUseCase:
    def __init__(self, repository: GenreRepository):
        self._repository = repository

    async def execute(self) -> list[Genre]:
        return await self._repository.get_all()
