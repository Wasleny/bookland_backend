from bookland.domain.repositories.review_repository import ReviewRepository


class DeleteReviewUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    async def execute(self, review_id: str) -> None:
        await self._repository.delete(review_id)
