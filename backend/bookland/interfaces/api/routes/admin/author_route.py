from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from uuid import uuid4

from bookland.domain.entities import Author
from bookland.domain.value_objects import Name
from bookland.interfaces.api.services import (
    get_get_author_usecase,
    get_create_author_usecase,
    get_update_author_usecase,
    get_soft_delete_author_usecase,
    get_get_all_authors_usecase,
)
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
async def create_author(
    author: CreateAuthorSchema,
    usecase=Depends(get_create_author_usecase),
):
    new_author = Author(str(uuid4()), Name(author.name), author.nationality)

    created_author = await usecase.execute(new_author)

    JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=author_messages.CREATE_AUTHOR_MESSAGE,
            data={"author": AuthorResponseSchema.from_entity(created_author)},
        ).model_dump(),
    )


@router.get(
    "/",
    response_model=ResponseEnvelopeSchema,
    responses={**ALL_AUTHORS_SUCCESS_RESPONSE},
)
async def get_all_authors(usecase=Depends(get_get_all_authors_usecase)):
    authors = await usecase.execute()

    if len(authors) == 0:
        return empty_search_result_response()

    JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=author_messages.GET_ALL_AUTHORS_MESSAGE,
            data={
                "authors": [
                    AuthorResponseSchema.from_entity(author) for author in authors
                ]
            },
        ).model_dump(),
    )


@router.get(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**AUTHOR_SUCCESS_RESPONSE, **AUTHOR_NOT_FOUND_RESPONSE},
)
async def get_author(id: str, get_author=Depends(get_get_author_usecase)):
    author = await _get_existing_author_or_404(id, get_author)

    JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=author_messages.GET_AUTHOR_MESSAGE,
            data={"author": AuthorResponseSchema.from_entity(author)},
        ).model_dump(),
    )


@router.patch(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**AUTHOR_SUCCESS_RESPONSE, **AUTHOR_NOT_FOUND_RESPONSE},
)
async def update_author(
    id: str,
    author: UpdateAuthorSchema,
    usecase=Depends(get_update_author_usecase),
    get_author=Depends(get_get_author_usecase),
):
    await _get_existing_author_or_404(id, get_author)

    updated_author = await usecase.execute(
        Author(id, Name(author.name), author.nationality)
    )

    JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=author_messages.UPDATE_AUTHOR_MESSAGE,
            data={"author": AuthorResponseSchema.from_entity(updated_author)},
        ).model_dump(),
    )


@router.delete(
    "/{id}",
    response_model=ResponseEnvelopeSchema,
    responses={**AUTHOR_NOT_FOUND_RESPONSE, **EMPTY_SUCCESS_RESPONSE},
)
async def delete_author(
    id: str,
    usecase=Depends(get_soft_delete_author_usecase),
    get_author=Depends(get_get_author_usecase),
):
    author = await _get_existing_author_or_404(id, get_author)
    await usecase.execute(id)

    JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ResponseEnvelopeSchema(
            message=author_messages.DELETE_AUTHOR_MESSAGE,
            data={"author": AuthorResponseSchema.from_entity(author)},
        ).model_dump(),
    )


async def _get_existing_author_or_404(id: str, get_author) -> Author:
    author = await get_author.execute(id)

    if not author:
        raise author_not_found_exception()

    return author
