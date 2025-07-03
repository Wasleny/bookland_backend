from bookland.infra.repositories import MongoGenreRepository
from bookland.application.usecases import GetAllGenresUseCase


repository = MongoGenreRepository()

get_all_genres_usecase = GetAllGenresUseCase(repository)
