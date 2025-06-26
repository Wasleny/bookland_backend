from bookland.domain.entities.review import Review
from bookland.domain.repositories.review_repository import ReviewRepository


class GetMostRecentReviewReadingUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    def execute(self, user_id: str, book_id: str) -> Review | None:
        return self._repository.get_most_recent_reading(user_id, book_id)
