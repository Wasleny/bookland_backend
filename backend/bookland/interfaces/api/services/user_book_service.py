from fastapi import Depends

from bookland.infra.repositories import MongoUserBookRepository
from bookland.application.usecases import (
    GetUserBookByUserUseCase,
    GetUserBookByUserAndBookUseCase,
    GetUserBookByIdUseCase,
    CreateUserBookUseCase,
    UpdateUserBookUseCase,
    DeleteUserBookUseCase,
)


def get_user_book_repository() -> MongoUserBookRepository:
    return MongoUserBookRepository()


def get_get_user_book_by_user_usecase(
    repository: MongoUserBookRepository = Depends(get_user_book_repository),
) -> GetUserBookByUserUseCase:
    return GetUserBookByUserUseCase(repository)


def get_get_user_book_by_user_and_book_usecase(
    repository: MongoUserBookRepository = Depends(get_user_book_repository),
) -> GetUserBookByUserAndBookUseCase:
    return GetUserBookByUserAndBookUseCase(repository)


def get_get_user_books_by_id_usecase(
    repository: MongoUserBookRepository = Depends(get_user_book_repository),
) -> GetUserBookByIdUseCase:
    return GetUserBookByIdUseCase(repository)


def get_create_user_book_usecase(
    repository: MongoUserBookRepository = Depends(get_user_book_repository),
) -> CreateUserBookUseCase:
    return CreateUserBookUseCase(repository)


def get_update_user_book_usecase(
    repository: MongoUserBookRepository = Depends(get_user_book_repository),
) -> UpdateUserBookUseCase:
    return UpdateUserBookUseCase(repository)


def get_delete_user_book_usecase(
    repository: MongoUserBookRepository = Depends(get_user_book_repository),
) -> DeleteUserBookUseCase:
    return DeleteUserBookUseCase(repository)
