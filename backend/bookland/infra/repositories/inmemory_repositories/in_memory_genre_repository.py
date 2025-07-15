from bookland.domain.entities import Genre
from bookland.domain.repositories import GenreRepository


class InMemoryGenreRepository(GenreRepository):
    def __init__(self) -> None:
        self._genres: dict[str, Genre] = {
            "1": {
                "id": "1",
                "name": "Fantasy",
                "name_pt_br": "Fantasia",
                "slug": "fantasy",
            },
            "2": {
                "id": "2",
                "name": "Fiction",
                "name_pt_br": "Ficção",
                "slug": "fiction",
            },
        }

    async def get_all(self) -> list[Genre]:
        return [genre for genre in self._genres.values()]
