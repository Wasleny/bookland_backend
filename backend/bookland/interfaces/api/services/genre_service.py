from fastapi import Depends

from bookland.infra.repositories import MongoGenreRepository
from bookland.application.usecases import GetAllGenresUseCase


def get_genre_repository() -> MongoGenreRepository:
    return MongoGenreRepository()


def get_get_all_genres_usecase(
    repository: MongoGenreRepository = Depends(get_genre_repository),
) -> GetAllGenresUseCase:
    return GetAllGenresUseCase(repository)
