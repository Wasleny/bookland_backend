from typing import Any

user_book_example = {
    "id": "string",
    "user_book_id": "string",
    "book_id": "string",
    "default_bookshelf_id": "string",
}

USER_BOOK_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "example": {
                    "message": "Operação concluída com sucesso.",
                    "data": {"user_book": user_book_example},
                }
            }
        },
    }
}

USER_BOOK_NOT_FOUND_RESPONSE: dict[int | str, dict[str, Any]] = {
    404: {
        "description": "Relação usuário-livro não encontrada.",
        "content": {
            "application/json": {
                "example": {"message": "Relação usuário-livro não encontrada."}
            }
        },
    }
}


ALL_USER_BOOK_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "examples": {
                    "Existe relação usuário-livro cadastrada(s)": {
                        "value": {
                            "message": "Operação concluída com sucesso.",
                            "data": {"user_book": [user_book_example]},
                        }
                    },
                    "Não existe usuário-livro cadastrada(s)": {
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
