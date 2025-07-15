from typing import Any

series_example = {
    "id": "string",
    "name": "string",
}

SERIES_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "example": {
                    "message": "Operação concluída com sucesso.",
                    "data": {"series": series_example},
                }
            }
        },
    }
}

SERIES_NOT_FOUND_RESPONSE: dict[int | str, dict[str, Any]] = {
    404: {
        "description": "Série não encontrada.",
        "content": {
            "application/json": {"example": {"message": "Série não encontrada."}}
        },
    }
}

ALL_SERIES_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "examples": {
                    "Existe série(s) cadastrada(s)": {
                        "value": {
                            "message": "Operação concluída com sucesso.",
                            "data": {"series": [series_example]},
                        }
                    },
                    "Não existe série(s) cadastrada(s)": {
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
