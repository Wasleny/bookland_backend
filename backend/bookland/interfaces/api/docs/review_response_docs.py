from typing import Any

review_example = {
    "id": "string",
    "user": {
        "id": "string",
        "name": "string",
        "ratings_count": 0,
        "reviews_count": 0,
        "average_rating": 0.0,
        "avatar": "string",
    },
    "book_id": "string",
    "rating": 0,
    "body": "string",
    "spoiler": False,
    "start_date": "2025-01-01",
    "end_date": "2025-01-01",
    "most_recent_reading": True,
    "rating_composition_criteria": [
        {"criterion": "string", "rating": 0},
    ],
    "independent_rating_criteria": [
        {"criterion": "string", "rating": 0},
    ],
}

REVIEW_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "example": {
                    "message": "Operação concluída com sucesso.",
                    "data": {"review": review_example},
                }
            }
        },
    }
}

REVIEW_NOT_FOUND_RESPONSE: dict[int | str, dict[str, Any]] = {
    404: {
        "description": "Resenha não encontrado.",
        "content": {
            "application/json": {"example": {"message": "Resenha não encontrado."}}
        },
    }
}

ALL_REVIEWS_SUCCESS_RESPONSE: dict[int | str, dict[str, Any]] = {
    200: {
        "description": "Operação realizada com sucesso.",
        "content": {
            "application/json": {
                "examples": {
                    "Existe resenha(s) cadastrada(s)": {
                        "value": {
                            "message": "Operação concluída com sucesso.",
                            "data": {"reviews": [review_example]},
                        }
                    },
                    "Não existe resenha(s) cadastrada(s)": {
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
