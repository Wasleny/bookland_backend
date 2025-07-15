from bookland.domain.entities import Review
from bookland.domain.repositories import ReviewRepository


class GetReviewsByBookUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    async def execute(self, book_id: str) -> list[Review]:
        return await self._repository.get_by_book(book_id)
