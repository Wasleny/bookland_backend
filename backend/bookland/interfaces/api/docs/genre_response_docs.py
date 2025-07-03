from typing import Any

genre_example = {
    "id": "string",
    "name": "string",
    "slug": "string",
}

GENRES_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "example": {
                    "message": "Operação concluída com sucesso.",
                    "data": {"genres": genre_example},
                }
            }
        },
    }
}
