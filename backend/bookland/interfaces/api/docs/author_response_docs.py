from typing import Any

author_example = {
    "id": "string",
    "name": "string",
    "nationality": "string",
}

AUTHOR_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "example": {
                    "message": "Operação concluída com sucesso.",
                    "data": {"author": author_example},
                }
            }
        },
    }
}

AUTHOR_NOT_FOUND_RESPONSE: dict[int | str, dict[str, Any]] = {
    404: {
        "description": "Autor não encontrado.",
        "content": {
            "application/json": {"example": {"message": "Autor não encontrado."}}
        },
    }
}

ALL_AUTHORS_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "examples": {
                    "Existe autor(es) cadastrado(s)": {
                        "value": {
                            "message": "Operação concluída com sucesso.",
                            "data": {"authors": [author_example]},
                        }
                    },
                    "Não existe autor(es) cadastrado(s)": {
                        "value": {
                            "message": "Operação concluída com sucesso.",
                            "data": {},
                        },
                    },
                }
            }
        },
    }
}
