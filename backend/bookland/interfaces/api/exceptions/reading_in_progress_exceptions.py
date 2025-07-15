from fastapi.exceptions import HTTPException
from fastapi import status

READING_IN_PROGRESS_NOT_FOUND_MESSAGE = "Leitura em progresso não encontrada."


def reading_in_progress_not_found_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=READING_IN_PROGRESS_NOT_FOUND_MESSAGE,
    )
