from bookland.infra.repositories import MongoAuthorRepository
from bookland.application.usecases import (
    CreateAuthorUseCase,
    GetAllAuthorsUseCase,
    GetAuthorByIdUseCase,
    SoftDeleteAuthorUseCase,
    UpdateAuthorUseCase,
)


repository = MongoAuthorRepository()

create_author_usecase = CreateAuthorUseCase(repository)
update_author_usecase = UpdateAuthorUseCase(repository)
get_author_usecase = GetAuthorByIdUseCase(repository)
get_all_authors_usecase = GetAllAuthorsUseCase(repository)
soft_delete_author_usecase = SoftDeleteAuthorUseCase(repository)
