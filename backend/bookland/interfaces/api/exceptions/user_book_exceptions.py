from fastapi.exceptions import HTTPException
from fastapi import status

USER_BOOK_NOT_FOUND_MESSAGE = "Relação usuário-livro não encontrada."


def user_book_not_found_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=USER_BOOK_NOT_FOUND_MESSAGE,
    )
