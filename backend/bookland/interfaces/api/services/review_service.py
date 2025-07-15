from bookland.infra.repositories import MongoReviewRepository
from bookland.application.usecases import (
    GetReviewByIdUseCase,
    GetReviewsByBookUseCase,
    GetReviewsByUserAndBookUseCase,
    GetMostRecentReviewReadingUseCase,
    CreateReviewUseCase,
    UpdateReviewUseCase,
    DeleteReviewUseCase,
    DeleteAllReviewsForUserAndBookUseCase,
)

repository = MongoReviewRepository()

get_review_by_id_usecase = GetReviewByIdUseCase(repository)
get_reviews_by_book_usecase = GetReviewsByBookUseCase(repository)
get_reviews_by_user_and_book_usecase = GetReviewsByUserAndBookUseCase(repository)
get_most_recent_review_reading_usecase = GetMostRecentReviewReadingUseCase(repository)
create_review_usecase = CreateReviewUseCase(repository)
update_review_usecase = UpdateReviewUseCase(repository)
delete_review_usecase = DeleteReviewUseCase(repository)
delete_all_reviews_for_user_and_book_usecase = DeleteAllReviewsForUserAndBookUseCase
