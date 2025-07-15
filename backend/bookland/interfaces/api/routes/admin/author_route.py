from fastapi import APIRouter, Depends
from uuid import uuid4

from bookland.domain.entities import Author
from bookland.domain.value_objects import Name
from bookland.interfaces.api.services import author_service
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
    empty_search_result_response,
)
from bookland.interfaces.api.exceptions import author_not_found_exception
from bookland.interfaces.api.messages import author_messages


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

    created_author = await author_service.create_author_usecase.execute(new_author)

    return ResponseEnvelopeSchema(
        message=author_messages.CREATE_AUTHOR_MESSAGE,
        data={"author": AuthorResponseSchema.from_entity(created_author)},
    )


@router.get(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**ALL_AUTHORS_SUCCESS_RESPONSE},
)
async def get_all_authors():
    authors = await author_service.get_all_authors_usecase.execute()

    if len(authors) == 0:
        return empty_search_result_response()

    return ResponseEnvelopeSchema(
        message=author_messages.GET_ALL_AUTHORS_MESSAGE,
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
    author = await _get_existing_author_or_404(id)

    return ResponseEnvelopeSchema(
        message=author_messages.GET_AUTHOR_MESSAGE,
        data={"author": AuthorResponseSchema.from_entity(author)},
    )


@router.patch(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**AUTHOR_SUCCESS_RESPONSE, **AUTHOR_NOT_FOUND_RESPONSE},
)
async def update_author(id: str, author: UpdateAuthorSchema):
    await _get_existing_author_or_404(id)

    updated_author = await author_service.update_author_usecase.execute(
        Author(id, Name(author.name), author.nationality)
    )

    return ResponseEnvelopeSchema(
        message=author_messages.UPDATE_AUTHOR_MESSAGE,
        data={"author": AuthorResponseSchema.from_entity(updated_author)},
    )


@router.delete(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**AUTHOR_NOT_FOUND_RESPONSE, **EMPTY_SUCCESS_RESPONSE},
)
async def delete_author(id: str):
    author = await _get_existing_author_or_404(id)
    await author_service.soft_delete_author_usecase.execute(id)

    return ResponseEnvelopeSchema(
        message=author_messages.DELETE_AUTHOR_MESSAGE,
        data={"author": AuthorResponseSchema.from_entity(author)},
    )


async def _get_existing_author_or_404(id: str) -> Author:
    author = await author_service.get_author_usecase.execute(id)

    if not author:
        raise author_not_found_exception()

    return author
