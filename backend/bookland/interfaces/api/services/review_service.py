from fastapi import Depends

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


def get_review_repository() -> MongoReviewRepository:
    return MongoReviewRepository()


def get_get_review_by_id_usecase(
    repository: MongoReviewRepository = Depends(get_review_repository),
) -> GetReviewByIdUseCase:
    return GetReviewByIdUseCase(repository)


def get_get_reviews_by_book_usecase(
    repository: MongoReviewRepository = Depends(get_review_repository),
) -> GetReviewsByBookUseCase:
    return GetReviewsByBookUseCase(repository)


def get_get_reviews_by_user_and_book_usecase(
    repository: MongoReviewRepository = Depends(get_review_repository),
) -> GetReviewsByUserAndBookUseCase:
    return GetReviewsByUserAndBookUseCase(repository)


def get_get_most_recent_review_reading_usecase(
    repository: MongoReviewRepository = Depends(get_review_repository),
) -> GetMostRecentReviewReadingUseCase:
    return GetMostRecentReviewReadingUseCase(repository)


def get_create_review_usecase(
    repository: MongoReviewRepository = Depends(get_review_repository),
) -> CreateReviewUseCase:
    return CreateReviewUseCase(repository)


def get_update_review_usecase(
    repository: MongoReviewRepository = Depends(get_review_repository),
) -> UpdateReviewUseCase:
    return UpdateReviewUseCase(repository)


def get_delete_review_usecase(
    repository: MongoReviewRepository = Depends(get_review_repository),
) -> DeleteReviewUseCase:
    return DeleteReviewUseCase(repository)


def get_delete_all_reviews_for_user_and_book_usecase(
    repository: MongoReviewRepository = Depends(get_review_repository),
) -> DeleteAllReviewsForUserAndBookUseCase:
    return DeleteAllReviewsForUserAndBookUseCase(repository)
