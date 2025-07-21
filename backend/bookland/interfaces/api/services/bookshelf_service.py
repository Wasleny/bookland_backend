from fastapi import Depends

from bookland.infra.repositories import MongoBookshelfRepository
from bookland.application.usecases import GetAllBookshelvesUseCase


def get_bookshelf_repository() -> MongoBookshelfRepository:
    return MongoBookshelfRepository()


def get_get_all_bookshelves_use_case(
    repository: MongoBookshelfRepository = Depends(get_bookshelf_repository),
) -> GetAllBookshelvesUseCase:
    return GetAllBookshelvesUseCase(repository)
