from bookland.infra.repositories import MongoReadingInProgressRepository
from bookland.application.usecases import (
    GetReadingInProgressByUserUseCase,
    GetReadingInProgressByUserAndBookUseCase,
    GetReadingInProgressByIdUseCase,
    CreateReadingInProgressUseCase,
    UpdateReadingInProgressUseCase,
    DeleteReadingInProgressUseCase,
)

repository = MongoReadingInProgressRepository()

get_reading_in_progress_by_user_usecase = GetReadingInProgressByUserUseCase(repository)
get_reading_in_progress_by_user_and_book_usecase = (
    GetReadingInProgressByUserAndBookUseCase(repository)
)
get_reading_in_progress_by_id_usecase = GetReadingInProgressByIdUseCase(repository)
create_reading_in_progress_usecase = CreateReadingInProgressUseCase(repository)
update_reading_in_progress_usecase = UpdateReadingInProgressUseCase(repository)
delete_reading_in_progress_usecase = DeleteReadingInProgressUseCase(repository)
