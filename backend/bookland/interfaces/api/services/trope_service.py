from fastapi import Depends

from bookland.infra.repositories import MongoTropeRepository
from bookland.application.usecases import GetAllTropesUseCase


def get_trope_repository() -> MongoTropeRepository:
    return MongoTropeRepository()


def get_get_all_tropes_usecase(
    repository: MongoTropeRepository = Depends(get_trope_repository),
) -> GetAllTropesUseCase:
    return GetAllTropesUseCase(repository)
