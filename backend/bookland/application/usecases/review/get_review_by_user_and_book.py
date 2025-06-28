from bookland.domain.entities.review import Review
from bookland.domain.repositories.review_repository import ReviewRepository


class GetReviewsByUserAndBookUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    async def execute(self, user_id: str, book_id: str) -> list[Review]:
        return await self._repository.get_by_user_and_book(user_id, book_id)
