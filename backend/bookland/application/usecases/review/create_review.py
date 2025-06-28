from bookland.domain.entities.review import Review
from bookland.domain.repositories.review_repository import ReviewRepository


class CreateReviewUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    async def execute(self, review: Review) -> Review:
        return await self._repository.create(review)
