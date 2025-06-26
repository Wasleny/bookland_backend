from bookland.domain.repositories.review_repository import ReviewRepository


class DeleteReviewUseCase:
    def __init__(self, repository: ReviewRepository):
        self._repository = repository

    def execute(self, review_id: str) -> None:
        self._repository.delete(review_id)
