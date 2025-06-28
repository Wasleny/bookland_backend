from bookland.domain.entities.review import Review
from bookland.domain.repositories.review_repository import ReviewRepository


class GetMostRecentReviewReadingUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    async def execute(self, user_id: str, book_id: str) -> Review | None:
        return await self._repository.get_most_recent_reading(user_id, book_id)
