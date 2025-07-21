from fastapi import Depends

from bookland.infra.repositories import MongoReadingInProgressRepository
from bookland.application.usecases import (
    GetReadingInProgressByUserUseCase,
    GetReadingInProgressByUserAndBookUseCase,
    GetReadingInProgressByIdUseCase,
    CreateReadingInProgressUseCase,
    UpdateReadingInProgressUseCase,
    DeleteReadingInProgressUseCase,
)


def get_reading_in_progress_repository() -> MongoReadingInProgressRepository:
    return MongoReadingInProgressRepository()


def get_get_reading_in_progress_by_user_usecase(
    repository: MongoReadingInProgressRepository = Depends(
        get_reading_in_progress_repository
    ),
) -> GetReadingInProgressByUserUseCase:
    return GetReadingInProgressByUserUseCase(repository)


def get_get_reading_in_progress_by_user_and_book_usecase(
    repository: MongoReadingInProgressRepository = Depends(
        get_reading_in_progress_repository
    ),
) -> GetReadingInProgressByUserAndBookUseCase:
    return GetReadingInProgressByUserAndBookUseCase(repository)


def get_get_reading_in_progress_by_id_usecase(
    repository: MongoReadingInProgressRepository = Depends(
        get_reading_in_progress_repository
    ),
) -> GetReadingInProgressByIdUseCase:
    return GetReadingInProgressByIdUseCase(repository)


def get_create_reading_in_progress_usecase(
    repository: MongoReadingInProgressRepository = Depends(
        get_reading_in_progress_repository
    ),
) -> CreateReadingInProgressUseCase:
    return CreateReadingInProgressUseCase(repository)


def get_update_reading_in_progress_usecase(
    repository: MongoReadingInProgressRepository = Depends(
        get_reading_in_progress_repository
    ),
) -> UpdateReadingInProgressUseCase:
    return UpdateReadingInProgressUseCase(repository)


def get_delete_reading_in_progress_usecase(
    repository: MongoReadingInProgressRepository = Depends(
        get_reading_in_progress_repository
    ),
) -> DeleteReadingInProgressUseCase:
    return DeleteReadingInProgressUseCase(repository)
