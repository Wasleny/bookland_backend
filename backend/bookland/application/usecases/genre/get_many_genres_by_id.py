from bookland.domain.repositories import GenreRepository
from bookland.domain.entities import Genre


class GetManyGenresByIdUseCase:
    def __init__(self, repository: GenreRepository):
        self._repository = repository

    async def execute(self, genre_ids: list[str]) -> list[Genre]:
        return await self._repository.get_many_by_id(genre_ids)
