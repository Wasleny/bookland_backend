from bookland.domain.entities.review import Review
from bookland.domain.repositories.review_repository import ReviewRepository


class UpdateReviewUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    async def execute(self, review: Review) -> Review | None:
        return await self._repository.update(review)
