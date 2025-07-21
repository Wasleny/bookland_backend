from fastapi import Depends

from bookland.infra.repositories import MongoAuthorRepository
from bookland.application.usecases import (
    CreateAuthorUseCase,
    GetAllAuthorsUseCase,
    GetAuthorByIdUseCase,
    SoftDeleteAuthorUseCase,
    UpdateAuthorUseCase,
)


def get_author_repository() -> MongoAuthorRepository:
    return MongoAuthorRepository()


def get_create_author_usecase(
    repository: MongoAuthorRepository = Depends(get_author_repository),
) -> CreateAuthorUseCase:
    return CreateAuthorUseCase(repository)


def get_update_author_usecase(
    repository: MongoAuthorRepository = Depends(get_author_repository),
) -> UpdateAuthorUseCase:
    return UpdateAuthorUseCase(repository)


def get_get_author_usecase(
    repository: MongoAuthorRepository = Depends(get_author_repository),
) -> GetAuthorByIdUseCase:
    return GetAuthorByIdUseCase(repository)


def get_get_all_authors_usecase(
    repository: MongoAuthorRepository = Depends(get_author_repository),
) -> GetAllAuthorsUseCase:
    return GetAllAuthorsUseCase(repository)


def get_soft_delete_author_usecase(
    repository: MongoAuthorRepository = Depends(get_author_repository),
) -> SoftDeleteAuthorUseCase:
    return SoftDeleteAuthorUseCase(repository)
