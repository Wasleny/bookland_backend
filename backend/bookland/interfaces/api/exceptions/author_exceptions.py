from fastapi.exceptions import HTTPException
from fastapi import status

AUTHOR_NOT_FOUND_MESSAGE = "Autor não encontrado."


def author_not_found_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=AUTHOR_NOT_FOUND_MESSAGE,
    )
