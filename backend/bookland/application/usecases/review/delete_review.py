from bookland.domain.repositories import ReviewRepository
from bookland.domain.entities import Review


class DeleteReviewUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    async def execute(self, review_id: str) -> Review | None:
        return await self._repository.delete(review_id)
