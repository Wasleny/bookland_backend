from bookland.domain.entities import Review
from bookland.domain.repositories import ReviewRepository


class InMemoryReviewRepository(ReviewRepository):
    def __init__(self) -> None:
        self._reviews: dict[str, Review] = {}

    async def get_by_id(self, review_id: str) -> Review | None:
        return self._reviews.get(review_id)

    async def get_by_book(self, book_id: str) -> list[Review]:
        return [
            review for review in self._reviews.values() if review.book_id == book_id
        ]

    async def get_by_user_and_book(self, user_id: str, book_id: str) -> list[Review]:
        return [
            review
            for review in self._reviews.values()
            if review.book_id == book_id and review.user_id == user_id
        ]

    async def get_book_most_recent_reading(
        self, user_id: str, book_id: str
    ) -> Review | None:
        for review in self._reviews.values():
            if (
                review.book_id == book_id
                and review.user_id == user_id
                and review.most_recent_reading
            ):
                return review
        return None

    async def create(self, review: Review) -> Review:
        self._reviews[review.id] = review

        return review

    async def update(self, review: Review) -> Review | None:
        if review.id in self._reviews:
            self._reviews[review.id] = review
            return review

        return None

    async def delete(self, review_id: str) -> Review | None:
        if review_id in self._reviews:
            review = self._reviews.get(review_id)
            self._reviews.pop(review_id, None)
            return review

        return None

    async def delete_all_for_user_and_book(
        self, user_id: str, book_id: str
    ) -> list[Review]:
        to_delete = [
            review
            for review in self._reviews.values()
            if review.book_id == book_id and review.user_id == user_id
        ]

        for review in to_delete:
            self._reviews.pop(review.id, None)

        return to_delete
