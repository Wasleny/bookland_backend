from bookland.domain.repositories.book_repository import BookRepository


class SoftDeleteBookUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    async def execute(self, book_id: str) -> None:
        await self._repository.soft_delete(book_id)
