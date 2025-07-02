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
)
from bookland.interfaces.api.responses import (
    author_not_found_response,
    bad_request_response,
    empty_search_result_response,
)


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

    try:
        created_author = await create_author_usecase.execute(new_author)

        return ResponseEnvelopeSchema(
            message="Autor cadastrado com sucesso.",
            data={"author": AuthorResponseSchema.from_entity(created_author)},
        )
    except Exception as e:
        return bad_request_response(str(e))


@router.get(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**AUTHOR_SUCCESS_RESPONSE, **AUTHOR_NOT_FOUND_RESPONSE},
)
async def get_author(id: str):
    author = await get_author_usecase.execute(id)

    if not author:
        return author_not_found_response()

    return ResponseEnvelopeSchema(
        message="Autor encontrado.",
        data={"author": AuthorResponseSchema.from_entity(author)},
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


@router.patch("/{id}", response_model=ResponseEnvelopeSchema)
async def update_author(id: str, author: UpdateAuthorSchema):
    updated_author = Author(id, Name(author.name), author.nationality)

    try:
        updated_author = await update_author_usecase.execute(updated_author)

        return ResponseEnvelopeSchema(
            message="Autor editado com sucesso.",
            data={"author": AuthorResponseSchema.from_entity(updated_author)},
        )
    except Exception as e:
        return bad_request_response(str(e))


@router.delete("/{id}", response_model=ResponseEnvelopeSchema)
async def delete_author(id: str):
    try:
        await soft_delete_author_usecase.execute(id)

        return ResponseEnvelopeSchema(message="Author excluído com sucesso.", data={})

    except Exception as e:
        return bad_request_response(str(e))
