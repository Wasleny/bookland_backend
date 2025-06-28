from fastapi.exceptions import HTTPException
from fastapi import status

USER_NOT_FOUND_MESSAGE = "Usuário não encontrado."
UNAUTHORIZED_MESSAGE = "Acesso não autorizado."
FORBIDDEN_MESSAGE = "Você não tem permissão para acessar este recurso."


def user_not_found_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=USER_NOT_FOUND_MESSAGE,
    )


def unauthorized_exception(message: str = UNAUTHORIZED_MESSAGE) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=message,
    )


def forbidden_exception(
    message: str = FORBIDDEN_MESSAGE,
) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=message,
    )
