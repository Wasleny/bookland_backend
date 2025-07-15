from fastapi.exceptions import HTTPException
from fastapi import status

BOOK_NOT_FOUND_MESSAGE = "Livro não encontrado."


def book_not_found_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=BOOK_NOT_FOUND_MESSAGE,
    )
