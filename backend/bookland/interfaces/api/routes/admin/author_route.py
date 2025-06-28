from fastapi import APIRouter, HTTPException
from uuid import uuid4
from bookland.domain.entities.author import Author
from bookland.domain.value_objects.name_vo import Name
from bookland.infra.repositories.mongo_repositories.mongo_author_repository import MongoAuthorRepository
from bookland.application.usecases.author.create_author import CreateAuthorUseCase
from bookland.application.usecases.author.get_all_authors import GetAllAuthorsUseCase
from bookland.application.usecases.author.get_author_by_id import GetAuthorByIdUseCase
from bookland.application.usecases.author.soft_delete_author import (
    SoftDeleteAuthorUseCase,
)
from bookland.application.usecases.author.update_author import UpdateAuthorUseCase
from bookland.interfaces.api.schemas.author import (
    AuthorCreateSchema,
    AuthorResponseSchema,
)

router = APIRouter()

repository = MongoAuthorRepository()


# create author
@router.post("/", response_model=AuthorResponseSchema)
async def create_author(author: AuthorCreateSchema):
    new_author = Author(str(uuid4()), Name(author.name), author.nationality)

    usecase = CreateAuthorUseCase(repository)
    created_author = await usecase.execute(new_author)

    return AuthorResponseSchema(
        id=created_author.id, name=created_author.name.value, nationality=created_author.nationality
    )


# get author by id
# @router.get("/author_id", response_model=AuthorResponseSchema)
# async def get_author(author_id: str):
#     usecase = GetAuthorByIdUseCase(repository)
#     author = await usecase.execute(author_id)

#     if not author:
#         raise HTTPException(status_code=404, detail="Autor não encontrado")

#     return AuthorResponseSchema(
#         id=author.id, name=author.name.value, nationality=author.nationality
#     )


# get all authors
# @router.get('/author_id', response_model=AuthorResponseSchema)


# soft_delete
# @router.get('/author_id', response_model=AuthorResponseSchema)

# update
# @router.get('/author_id', response_model=AuthorResponseSchema)
