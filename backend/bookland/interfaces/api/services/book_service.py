from fastapi import Depends

from bookland.infra.repositories import MongoBookRepository
from bookland.application.usecases import (
    CreateBookUseCase,
    GetBookByIdUseCase,
    GetAllBooksUseCase,
    UpdateBookUseCase,
    SoftDeleteBookUseCase,
    SearchBooksUseCase,
)


def get_book_repository() -> MongoBookRepository:
    return MongoBookRepository()


def get_create_book_use_case(
    repository: MongoBookRepository = Depends(get_book_repository),
) -> CreateBookUseCase:
    return CreateBookUseCase(repository)


def get_get_book_use_case(
    repository: MongoBookRepository = Depends(get_book_repository),
) -> GetBookByIdUseCase:
    return GetBookByIdUseCase(repository)


def get_get_all_books_use_case(
    repository: MongoBookRepository = Depends(get_book_repository),
) -> GetAllBooksUseCase:
    return GetAllBooksUseCase(repository)


def get_update_book_use_case(
    repository: MongoBookRepository = Depends(get_book_repository),
) -> UpdateBookUseCase:
    return UpdateBookUseCase(repository)


def get_soft_delete_book_use_case(
    repository: MongoBookRepository = Depends(get_book_repository),
) -> SoftDeleteBookUseCase:
    return SoftDeleteBookUseCase(repository)


def get_search_books_use_case(
    repository: MongoBookRepository = Depends(get_book_repository),
) -> SearchBooksUseCase:
    return SearchBooksUseCase(repository)
