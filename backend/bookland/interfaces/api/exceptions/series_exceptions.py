from fastapi.exceptions import HTTPException
from fastapi import status

SERIES_NOT_FOUND_MESSAGE = "Série não encontrada."


def series_not_found_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=SERIES_NOT_FOUND_MESSAGE,
    )
