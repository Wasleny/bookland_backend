from fastapi import Depends

from bookland.infra.repositories import MongoSeriesRepository
from bookland.application.usecases import (
    CreateSeriesUseCase,
    GetAllSeriesUseCase,
    GetSeriesByIdUseCase,
    SoftDeleteSeriesUseCase,
    UpdateSeriesUseCase,
)


def get_series_repository() -> MongoSeriesRepository:
    return MongoSeriesRepository()


def get_create_series_usecase(
    repository: MongoSeriesRepository = Depends(get_series_repository),
) -> CreateSeriesUseCase:
    return CreateSeriesUseCase(repository)


def get_get_all_series_usecase(
    repository: MongoSeriesRepository = Depends(get_series_repository),
) -> GetAllSeriesUseCase:
    return GetAllSeriesUseCase(repository)


def get_get_series_usecase(
    repository: MongoSeriesRepository = Depends(get_series_repository),
) -> GetSeriesByIdUseCase:
    return GetSeriesByIdUseCase(repository)


def get_soft_delete_series_usecase(
    repository: MongoSeriesRepository = Depends(get_series_repository),
) -> SoftDeleteSeriesUseCase:
    return SoftDeleteSeriesUseCase(repository)


def get_update_series_usecase(
    repository: MongoSeriesRepository = Depends(get_series_repository),
) -> UpdateSeriesUseCase:
    return UpdateSeriesUseCase(repository)
