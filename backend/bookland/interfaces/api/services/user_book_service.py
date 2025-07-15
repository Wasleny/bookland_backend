from bookland.infra.repositories import MongoUserBookRepository
from bookland.application.usecases import (
    GetUserBookByUserUseCase,
    GetUserBookByUserAndBookUseCase,
    GetUserBookByIdUseCase,
    CreateUserBookUseCase,
    UpdateUserBookUseCase,
    DeleteUserBookUseCase,
)

repository = MongoUserBookRepository()

get_user_book_by_user_usecase = GetUserBookByUserUseCase(repository)
get_user_book_by_user_and_book_usecase = GetUserBookByUserAndBookUseCase(repository)
get_user_books_by_id_usecase = GetUserBookByIdUseCase(repository)
create_user_book_usecase = CreateUserBookUseCase(repository)
update_user_book_usecase = UpdateUserBookUseCase(repository)
delete_user_book_usecase = DeleteUserBookUseCase(repository)
