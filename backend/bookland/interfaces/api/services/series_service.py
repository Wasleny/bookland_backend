from bookland.infra.repositories import MongoSeriesRepository
from bookland.application.usecases import (
    CreateSeriesUseCase,
    GetAllSeriesUseCase,
    GetSeriesByIdUseCase,
    SoftDeleteSeriesUseCase,
    UpdateSeriesUseCase,
)


repository = MongoSeriesRepository()

create_series_usecase = CreateSeriesUseCase(repository)
update_series_usecase = GetAllSeriesUseCase(repository)
get_series_usecase = GetSeriesByIdUseCase(repository)
get_all_series_usecase = SoftDeleteSeriesUseCase(repository)
soft_delete_series_usecase = UpdateSeriesUseCase(repository)
