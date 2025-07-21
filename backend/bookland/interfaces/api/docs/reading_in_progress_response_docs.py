from typing import Any

reading_in_progress_example = {
    "id": "string",
    "user_id": "string",
    "book_id": "string",
    "progress": 50,
}

READING_IN_PROGRESS_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "example": {
                    "message": "Operação concluída com sucesso.",
                    "data": {"readings_in_progress": reading_in_progress_example},
                }
            }
        },
    }
}

READING_IN_PROGRESS_NOT_FOUND_RESPONSE: dict[int | str, dict[str, Any]] = {
    404: {
        "description": "Leituras em progress não encontradas.",
        "content": {
            "application/json": {
                "example": {"message": "Leituras em progress não encontradas."}
            }
        },
    }
}

ALL_READING_IN_PROGRESSS_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "examples": {
                    "Existe leitura(s) em progresso cadastrada(s)": {
                        "value": {
                            "message": "Operação concluída com sucesso.",
                            "data": {
                                "reading_in_progresss": [reading_in_progress_example]
                            },
                        }
                    },
                    "Não existe leitura(s) em progresso cadastrada(s)": {
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
