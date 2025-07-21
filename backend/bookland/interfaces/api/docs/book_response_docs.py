from typing import Any

book_example = {
    "id": "string",
    "title": "string",
    "original_title": "string",
    "books": [
        {
            "id": "string",
            "name": "string",
        }
    ],
    "main_genre": "string",
    "secondary_genres": ["string"],
    "tropes": ["string"],
    "cover": "string",
    "series": "string",
    "original_series": "string",
    "book_number": 1,
    "average_rating": 4.5,
    "ratings_count": 1000,
    "reviews_count": 500,
    "synopsis": "string",
    "format": "string",
    "pages": 300,
    "publication_date": "2023-10-01",
    "publisher": "string",
    "isbn10": "string",
    "isbn13": "string",
    "asin": "string",
    "language": "string",
    "alternative_edition_ids": ["string"],
}

BOOK_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "example": {
                    "message": "Operação concluída com sucesso.",
                    "data": {"book": book_example},
                }
            }
        },
    }
}

BOOK_NOT_FOUND_RESPONSE: dict[int | str, dict[str, Any]] = {
    404: {
        "description": "Livro não encontrado.",
        "content": {
            "application/json": {"example": {"message": "Livro não encontrado."}}
        },
    }
}

ALL_BOOKS_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "examples": {
                    "Existe livro(s) cadastrado(s)": {
                        "value": {
                            "message": "Operação concluída com sucesso.",
                            "data": {"books": [book_example]},
                        }
                    },
                    "Não existe livro(s) cadastrado(s)": {
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
