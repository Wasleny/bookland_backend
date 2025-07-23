from fastapi import APIRouter, Depends, Query

from bookland.domain.entities import Book
from bookland.interfaces.api.services import (
    get_get_book_use_case,
    get_search_books_use_case,
    get_author_repository,
    get_genre_repository,
    get_trope_repository,
    get_series_repository,
)
from bookland.interfaces.api.schemas import book as book_schemas
from bookland.interfaces.api.deps import admin_required
from bookland.interfaces.api.docs import (
    BOOK_SUCCESS_RESPONSE,
    BOOK_NOT_FOUND_RESPONSE,
    FORBIDDEN_RESPONSE,
    USER_UNAUTHORIZED,
)
from bookland.interfaces.api.exceptions import book_not_found_exception
from bookland.interfaces.api.messages import book_messages


router = APIRouter(
    responses={**FORBIDDEN_RESPONSE, **USER_UNAUTHORIZED},
)


@router.get(
    "/{id}",
    response_model=book_schemas.BookResponseSchema,
    responses={**BOOK_SUCCESS_RESPONSE, **BOOK_NOT_FOUND_RESPONSE},
)
async def get_book(
    id: str,
    get_book=Depends(get_get_book_use_case),
    author_repo=Depends(get_author_repository),
    genre_repo=Depends(get_genre_repository),
    trope_repo=Depends(get_trope_repository),
    series_repo=Depends(get_series_repository),
):
    """
    Recupera um livro pelo seu ID.
    """
    book_found = await _get_existing_book_or_404(id, get_book)
    book_data = book_schemas.BookWithoutRelationsSchema.from_entity(
        book_found
    ).model_dump()
    book = await enrich_book_with_related_data(
        book_data, author_repo, genre_repo, trope_repo, series_repo
    )

    return book_schemas.BookResponseSchema.from_entity(
        book_schemas.BookDataSchema.model_validate(book),
        book_messages.GET_BOOK_MESSAGE,
    )


async def _get_existing_book_or_404(id: str, get_book) -> Book:
    book = await get_book.execute(id)

    if not book:
        raise book_not_found_exception()

    return book


async def enrich_book_with_related_data(
    book: dict, author_repo, genre_repo, trope_repo, series_repo
):
    authors = await author_repo.get_many_by_id(book["author_ids"])
    main_genre = await genre_repo.get_by_id(book["main_genre_id"])
    secondary_genres = await genre_repo.get_many_by_id(book["secondary_genre_ids"])
    tropes = await trope_repo.get_many_by_id(book["trope_ids"])
    series = await series_repo.get_by_id(book["series_id"])
    original_series = await series_repo.get_by_id(book["original_series_id"])

    book["authors"] = authors
    book["main_genre"] = main_genre
    book["secondary_genres"] = secondary_genres
    book["tropes"] = tropes
    book["series"] = series
    book["original_series"] = original_series

    return book
