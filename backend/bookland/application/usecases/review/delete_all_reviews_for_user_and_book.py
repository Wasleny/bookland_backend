from bookland.domain.repositories import ReviewRepository
from bookland.domain.entities import Review


class DeleteAllReviewsForUserAndBookUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    async def execute(self, user_id: str, book_id: str) -> list[Review]:
        return await self._repository.delete_all_for_user_and_book(user_id, book_id)
