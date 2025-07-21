from typing import Any

bookshelf_example = {
    "id": "string",
    "name": "string",
    "slug": "string",
}


ALL_BOOKSHELVES_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "examples": {
                    "Existe estante(s) cadastrada(s)": {
                        "value": {
                            "message": "Operação concluída com sucesso.",
                            "data": {"bookshelves": [bookshelf_example]},
                        }
                    },
                    "Não existe estante(s) cadastrada(s)": {
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
