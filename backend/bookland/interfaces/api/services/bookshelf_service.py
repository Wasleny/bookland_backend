from bookland.infra.repositories import MongoBookshelfRepository
from bookland.application.usecases import GetAllBookshelvesUseCase

repository = MongoBookshelfRepository()

get_all_bookshelves_use_case = GetAllBookshelvesUseCase(repository)
