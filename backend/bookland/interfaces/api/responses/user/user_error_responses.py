from fastapi.responses import JSONResponse
from fastapi import status

USER_NOT_FOUND_MESSAGE = "Usuário não encontrado."
UNAUTHORIZED_MESSAGE = "Acesso não autorizado."
FORBIDDEN_MESSAGE = "Você não tem permissão para acessar este recurso."
BAD_REQUEST_MESSAGE = "Dados inválidos ou incompletos fornecidos pelo usuário."


def user_not_found_response() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": USER_NOT_FOUND_MESSAGE},
    )


def unauthorized_response(message: str = UNAUTHORIZED_MESSAGE) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED, content={"message": message}
    )


def forbidden_response(
    message: str = FORBIDDEN_MESSAGE,
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN, content={"message": message}
    )


def bad_request_response(message: str = BAD_REQUEST_MESSAGE) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"message": message}
    )
