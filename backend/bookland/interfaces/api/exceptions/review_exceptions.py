from fastapi.exceptions import HTTPException
from fastapi import status

REVIEW_NOT_FOUND_MESSAGE = "Resenha não encontrada."


def review_not_found_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=REVIEW_NOT_FOUND_MESSAGE,
    )
