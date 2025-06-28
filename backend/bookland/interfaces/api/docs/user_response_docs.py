from typing import Any

user_example = {
    "id": "string",
    "name": "string",
    "nickname": "string",
    "email": "user@example.com",
    "gender": "male",
    "birthday": "2025-06-28",
    "avatar_url": "string",
    "role": "role",
}

USER_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "example": {
                    "message": "Operação concluída com sucesso.",
                    "data": {"user": user_example},
                }
            }
        },
    }
}

USER_NOT_FOUND_RESPONSE: dict[int | str, dict[str, Any]] = {
    404: {
        "description": "Usuário não encontrado.",
        "content": {
            "application/json": {"example": {"message": "Usuário não encontrado."}}
        },
    }
}

FORBIDDEN_RESPONSE: dict[int | str, dict[str, Any]] = {
    403: {
        "description": "Acesso negado.",
        "content": {
            "application/json": {
                "example": {"message": "Usuário não possui permissão de acesso."}
            }
        },
    }
}

USER_SEARCH_RESPONSES: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Respostas possíveis para a busca de usuário.",
        "content": {
            "application/json": {
                "examples": {
                    "Usuário encontrado": {
                        "value": {
                            "message": "Usuário encontrado com sucesso.",
                            "data": {"user": user_example},
                        }
                    },
                    "Usuário não encontrado": {
                        "value": {
                            "message": "Nenhum usuário encontrado.",
                            "data": {},
                        }
                    },
                }
            }
        },
    }
}

USER_BAD_REQUEST: dict[int | str, dict[str, Any]] = {
    400: {
        "description": "Requisição inválida.",
        "content": {
            "application/json": {
                "example": {
                    "message": "Dados inválidos ou incompletos fornecidos pelo usuário."
                }
            }
        },
    }
}

USER_UNAUTHORIZED: dict[int | str, dict[str, Any]] = {
    401: {
        "description": "Credenciais inválidas",
        "content": {
            "application/json": {"example": {"message": "Acesso não autorizado."}}
        },
    }
}
