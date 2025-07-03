from typing import Any

trope_example = {
    "id": "string",
    "name": "string",
    "slug": "string",
}

TROPES_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "example": {
                    "message": "Operação concluída com sucesso.",
                    "data": {"tropes": trope_example},
                }
            }
        },
    }
}
