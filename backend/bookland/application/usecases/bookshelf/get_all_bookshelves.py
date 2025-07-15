from bookland.domain.repositories import BookshelfRepository
from bookland.domain.entities import Bookshelf


class GetAllBookshelvesUseCase:
    def __init__(self, repository: BookshelfRepository):
        self._repository = repository

    async def execute(self) -> list[Bookshelf]:
        return await self._repository.get_all()
