from fastapi.responses import JSONResponse
from fastapi import status


def empty_search_result_response() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": [],
            "message": "Nenhum resultado foi encontrado.",
        },
    )
