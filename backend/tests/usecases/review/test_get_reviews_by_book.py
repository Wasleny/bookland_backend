from bookland.infra.repositories.in_memory_review_repository import InMemoryReviewRepository
from bookland.usecases.review.get_reviews_by_book import GetReviewsByBookUseCase
from tests.factories.review_factory import create_review

def test_get_reviews_by_book_returns_reviews():
    repository = InMemoryReviewRepository()
    usecase = GetReviewsByBookUseCase(repository)
    
    review1 = create_review()
    review2 = create_review(book_id=review1.book_id, most_recent_reading=True)
    repository.create(review1)
    repository.create(review2)

    reviews = usecase.execute(review1.book_id)

    assert len(reviews) == 2