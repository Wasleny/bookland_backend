from bookland.domain.entities import Review
from bookland.domain.repositories import ReviewRepository


class CreateReviewUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    async def execute(self, review: Review) -> Review:
        return await self._repository.create(review)
