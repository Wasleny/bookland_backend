from fastapi.exceptions import HTTPException
from fastapi import status

CRITERION_NOT_FOUND_MESSAGE = "Critério não encontrado."


def criterion_not_found_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=CRITERION_NOT_FOUND_MESSAGE,
    )
