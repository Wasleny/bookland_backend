from bookland.domain.entities import Review
from bookland.domain.repositories import ReviewRepository


class GetReviewByIdUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    async def execute(self, review_id: str) -> Review | None:
        return await self._repository.get_by_id(review_id)
