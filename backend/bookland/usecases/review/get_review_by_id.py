from bookland.domain.entities.review import Review
from bookland.domain.repositories.review_repository import ReviewRepository


class GetReviewByIdUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    def execute(self, review_id: str) -> Review | None:
        return self._repository.get_by_id(review_id)
