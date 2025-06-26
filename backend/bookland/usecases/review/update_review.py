from bookland.domain.entities.review import Review
from bookland.domain.repositories.review_repository import ReviewRepository


class UpdateReviewUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    def execute(self, review: Review) -> None:
        self._repository.update(review)
