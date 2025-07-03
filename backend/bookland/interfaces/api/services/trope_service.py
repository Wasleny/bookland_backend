from bookland.infra.repositories import MongoTropeRepository
from bookland.application.usecases import GetAllTropesUseCase


repository = MongoTropeRepository()

get_all_tropes_usecase = GetAllTropesUseCase(repository)
