from fastapi.responses import JSONResponse
from fastapi import status

AUTHOR_NOT_FOUND_MESSAGE = "Autor não encontrado."


def author_not_found_response() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": AUTHOR_NOT_FOUND_MESSAGE},
    )
