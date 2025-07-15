from bookland.domain.entities import Genre
from bookland.domain.repositories import GenreRepository


class InMemoryGenreRepository(GenreRepository):
    def __init__(self) -> None:
        self._genres: dict[str, Genre] = {}

    async def get_all(self) -> list[Genre]:
        return [genre for genre in self._genres.values()]
