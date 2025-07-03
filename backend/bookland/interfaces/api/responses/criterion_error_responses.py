from fastapi.responses import JSONResponse
from fastapi import status

CRITERION_NOT_FOUND_MESSAGE = "Critério não encontrado."


def criterion_not_found_response() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": CRITERION_NOT_FOUND_MESSAGE},
    )
