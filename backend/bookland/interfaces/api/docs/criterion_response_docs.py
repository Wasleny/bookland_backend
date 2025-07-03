from typing import Any

criterion_example = {
    "id": "string",
    "name": "string",
    "description": "string",
    "user_id": "string",
}

CRITERION_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "example": {
                    "message": "Operação concluída com sucesso.",
                    "data": {"criterion": criterion_example},
                }
            }
        },
    }
}

CRITERION_NOT_FOUND_RESPONSE: dict[int | str, dict[str, Any]] = {
    404: {
        "description": "Critério não encontrado.",
        "content": {
            "application/json": {"example": {"message": "Critério não encontrado."}}
        },
    }
}

CRITERIA_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "examples": {
                    "Encontrou critério(s)": {
                        "value": {
                            "message": "Operação concluída com sucesso.",
                            "data": {"criteria": [criterion_example]},
                        }
                    },
                    "Não encontrou critério(s)": {
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
