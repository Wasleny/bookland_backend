from bookland.domain.repositories.review_repository import ReviewRepository


class DeleteAllReviewsForUserAndBookUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    async def execute(self, user_id: str, book_id: str) -> None:
        await self._repository.delete_all_for_user_and_book(user_id, book_id)
