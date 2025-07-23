from fastapi import APIRouter, Depends
from uuid import uuid4
from datetime import date

from bookland.domain.entities import Book
from bookland.domain.value_objects import Title, Date, Slug, Isbn
from bookland.domain.enums import BookFormat
from bookland.interfaces.api.services import (
    get_create_book_use_case,
    get_get_book_use_case,
    get_get_all_books_use_case,
    get_update_book_use_case,
    get_soft_delete_book_use_case,
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
    ALL_BOOKS_SUCCESS_RESPONSE,
    FORBIDDEN_RESPONSE,
    USER_BAD_REQUEST,
    USER_UNAUTHORIZED,
    EMPTY_SUCCESS_RESPONSE,
)
from bookland.interfaces.api.responses import (
    empty_search_result_response,
)
from bookland.interfaces.api.exceptions import book_not_found_exception
from bookland.interfaces.api.messages import book_messages


router = APIRouter(
    dependencies=[Depends(admin_required)],
    responses={**FORBIDDEN_RESPONSE, **USER_UNAUTHORIZED},
)


@router.post(
    "/",
    response_model=book_schemas.BookResponseSchema,
    responses={**USER_BAD_REQUEST, **BOOK_SUCCESS_RESPONSE},
)
async def create_book(
    book: book_schemas.CreateBookSchema,
    usecase=Depends(get_create_book_use_case),
    author_repo=Depends(get_author_repository),
    genre_repo=Depends(get_genre_repository),
    trope_repo=Depends(get_trope_repository),
    series_repo=Depends(get_series_repository),
):
    """
    Cria um novo livro no sistema.
    """
    new_book = Book(
        str(uuid4()),
        Title(book.title),
        book.author_ids,
        book.main_genre_id,
        book.cover,
        book.synopsis,
        BookFormat(book.format),
        book.pages,
        Date(date.fromisoformat(book.publication_date)),
        book.language,
        Title(book.original_title),
        Slug(book.slug),
        book.secondary_genre_ids,
        book.trope_ids,
        book.series_id,
        book.original_series_id,
        book.book_number,
        book.publisher,
        Isbn(book.isbn10) if book.isbn10 is not None else None,
        Isbn(book.isbn13) if book.isbn13 is not None else None,
        book.asin,
        book.alternative_edition_ids,
    )
    created_book = await usecase.execute(new_book)
    book_data = book_schemas.BookWithoutRelationsSchema.from_entity(
        created_book
    ).model_dump()
    book = await enrich_book_with_related_data(
        book_data, author_repo, genre_repo, trope_repo, series_repo
    )

    return book_schemas.BookResponseSchema.from_entity(
        book_schemas.BookDataSchema.model_validate(book),
        book_messages.CREATE_BOOK_MESSAGE,
    )


@router.get(
    "/",
    response_model=book_schemas.AllBooksResponseSchema,
    responses={**ALL_BOOKS_SUCCESS_RESPONSE},
)
async def get_all_books(
    usecase=Depends(get_get_all_books_use_case),
    author_repo=Depends(get_author_repository),
    genre_repo=Depends(get_genre_repository),
    trope_repo=Depends(get_trope_repository),
    series_repo=Depends(get_series_repository),
):
    """
    Recupera todos os livros do sistema.
    """
    books = await usecase.execute()

    if len(books) == 0:
        return empty_search_result_response()

    for i in range(len(books)):
        book_data = book_schemas.BookWithoutRelationsSchema.from_entity(
            books[i]
        ).model_dump()
        books[i] = await enrich_book_with_related_data(
            book_data, author_repo, genre_repo, trope_repo, series_repo
        )

    return book_schemas.AllBooksResponseSchema.from_entity(
        [book_schemas.BookDataSchema.model_validate(book) for book in books],
        book_messages.GET_ALL_BOOKS_MESSAGE,
    )


@router.patch(
    "/{id}",
    response_model=book_schemas.BookResponseSchema,
    responses={**BOOK_SUCCESS_RESPONSE, **BOOK_NOT_FOUND_RESPONSE},
)
async def update_book(
    id: str,
    book: book_schemas.UpdateBookSchema,
    usecase=Depends(get_update_book_use_case),
    get_book=Depends(get_get_book_use_case),
    author_repo=Depends(get_author_repository),
    genre_repo=Depends(get_genre_repository),
    trope_repo=Depends(get_trope_repository),
    series_repo=Depends(get_series_repository),
):
    """
    Atualiza os dados de um livro pelo o ID.
    """
    await _get_existing_book_or_404(id, get_book)

    updated_book = await usecase.execute(
        Book(
            id,
            Title(book.title),
            book.author_ids,
            book.main_genre_id,
            book.cover,
            book.synopsis,
            BookFormat(book.format),
            book.pages,
            Date(date.fromisoformat(book.publication_date)),
            book.language,
            Title(book.original_title),
            Slug(book.slug),
            book.secondary_genre_ids,
            book.trope_ids,
            book.series_id,
            book.original_series_id,
            book.book_number,
            book.publisher,
            Isbn(book.isbn10) if book.isbn10 else None,
            Isbn(book.isbn13) if book.isbn13 else None,
            book.asin,
            book.alternative_edition_ids,
        )
    )

    book_data = book_schemas.BookWithoutRelationsSchema.from_entity(
        updated_book
    ).model_dump()
    book = await enrich_book_with_related_data(
        book_data, author_repo, genre_repo, trope_repo, series_repo
    )

    return book_schemas.BookResponseSchema.from_entity(
        book_schemas.BookDataSchema.model_validate(book),
        book_messages.UPDATE_BOOK_MESSAGE,
    )


@router.delete(
    "/{id}",
    response_model=book_schemas.BookResponseSchema,
    responses={**BOOK_NOT_FOUND_RESPONSE, **EMPTY_SUCCESS_RESPONSE},
)
async def delete_book(
    id: str,
    usecase=Depends(get_soft_delete_book_use_case),
    get_book=Depends(get_get_book_use_case),
    author_repo=Depends(get_author_repository),
    genre_repo=Depends(get_genre_repository),
    trope_repo=Depends(get_trope_repository),
    series_repo=Depends(get_series_repository),
):
    book = await _get_existing_book_or_404(id, get_book)
    await usecase.execute(id)

    book_data = book_schemas.BookWithoutRelationsSchema.from_entity(book).model_dump()
    book = await enrich_book_with_related_data(
        book_data, author_repo, genre_repo, trope_repo, series_repo
    )

    return book_schemas.BookResponseSchema.from_entity(
        book_schemas.BookDataSchema.model_validate(book),
        book_messages.DELETE_BOOK_MESSAGE,
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
