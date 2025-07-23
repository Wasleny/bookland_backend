from bookland.domain.repositories import GenreRepository
from bookland.domain.entities import Genre


class GetGenreByIdUseCase:
    def __init__(self, repository: GenreRepository):
        self._repository = repository

    async def execute(self, genre_id: str) -> Genre | None:
        return await self._repository.get_by_id(genre_id)
