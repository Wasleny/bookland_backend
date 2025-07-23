from bookland.domain.entities import Genre
from bookland.domain.repositories import GenreRepository


class InMemoryGenreRepository(GenreRepository):
    def __init__(self) -> None:
        self._genres: dict[str, Genre] = {}

    async def get_all(self) -> list[Genre]:
        return [genre for genre in self._genres.values()]

    async def get_by_id(self, genre_id):
        raise NotImplementedError("...")

    async def get_many_by_id(self, genre_ids):
        raise NotImplementedError("...")
