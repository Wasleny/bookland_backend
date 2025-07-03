from fastapi import APIRouter, Depends
from uuid import uuid4

from bookland.domain.entities.author import Author
from bookland.domain.value_objects import Name
from bookland.interfaces.api.services.author_service import *
from bookland.interfaces.api.schemas import (
    CreateAuthorSchema,
    UpdateAuthorSchema,
    AuthorResponseSchema,
    ResponseEnvelopeSchema,
)
from bookland.interfaces.api.deps import admin_required
from bookland.interfaces.api.docs import (
    AUTHOR_SUCCESS_RESPONSE,
    AUTHOR_NOT_FOUND_RESPONSE,
    ALL_AUTHORS_SUCCESS_RESPONSE,
    FORBIDDEN_RESPONSE,
    USER_BAD_REQUEST,
    USER_UNAUTHORIZED,
    EMPTY_SUCCESS_RESPONSE,
)
from bookland.interfaces.api.responses import (
    author_not_found_response,
    bad_request_response,
    empty_search_result_response,
)
from bookland.interfaces.api.exceptions import author_not_found_exception


router = APIRouter(
    dependencies=[Depends(admin_required)],
    responses={**FORBIDDEN_RESPONSE, **USER_UNAUTHORIZED},
)


@router.post(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**USER_BAD_REQUEST, **AUTHOR_SUCCESS_RESPONSE},
)
async def create_author(author: CreateAuthorSchema):
    new_author = Author(str(uuid4()), Name(author.name), author.nationality)

    created_author = await create_author_usecase.execute(new_author)

    return ResponseEnvelopeSchema(
        message="Autor cadastrado com sucesso.",
        data={"author": AuthorResponseSchema.from_entity(created_author)},
    )


@router.get(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**ALL_AUTHORS_SUCCESS_RESPONSE},
)
async def get_all_authors():
    authors = await get_all_authors_usecase.execute()

    if len(authors) == 0:
        return empty_search_result_response()

    return ResponseEnvelopeSchema(
        message="Autores encontrados.",
        data={
            "authors": [AuthorResponseSchema.from_entity(author) for author in authors]
        },
    )


@router.get(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**AUTHOR_SUCCESS_RESPONSE, **AUTHOR_NOT_FOUND_RESPONSE},
)
async def get_author(id: str):
    author = await _verify_existence(id)

    return ResponseEnvelopeSchema(
        message="Autor encontrado.",
        data={"author": AuthorResponseSchema.from_entity(author)},
    )


@router.patch(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**AUTHOR_SUCCESS_RESPONSE, **AUTHOR_NOT_FOUND_RESPONSE},
)
async def update_author(id: str, author: UpdateAuthorSchema):
    await _verify_existence(id)

    updated_author = await update_author_usecase.execute(
        Author(id, Name(author.name), author.nationality)
    )

    return ResponseEnvelopeSchema(
        message="Autor editado com sucesso.",
        data={"author": AuthorResponseSchema.from_entity(updated_author)},
    )


@router.delete(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**AUTHOR_NOT_FOUND_RESPONSE, **EMPTY_SUCCESS_RESPONSE},
)
async def delete_author(id: str):
    await _verify_existence(id)
    await soft_delete_author_usecase.execute(id)

    return ResponseEnvelopeSchema(message="Autor excluído com sucesso.", data={})


async def _verify_existence(id: str) -> Author:
    author = await get_author_usecase.execute(id)

    if not author:
        raise author_not_found_exception()

    return author
