class CommonErrors:
    INVALID_ID = "O ID deve ser uma string não vazia."
    INVALID_NAME = "O nome deve ser uma instância válida de Name."
    INVALID_LABEL = "O nome deve ser uma instância válida de Label."
    INVALID_LABEL_PT_BR = "O nome em português deve ser uma instância válida de Label."
    INVALID_TITLE = "O nome deve ser uma instância válida de Title."
    INVALID_SLUG = "O slug deve ser uma instância válida de Slug."
    INVALID_USER_ID = "O ID do usuário deve ser uma string não vazia."
    INVALID_BOOK_ID = "O ID do livro deve ser uma string não vazia."
    INVALID_DESCRIPTION = "A descrição deve ser uma string não vazia."
    INVALID_DELETED_AT = (
        "O campo deleted_at deve ser None ou uma instância válida de datetime."
    )
    INVALID_AVERAGE_RATING = (
        "A média de avaliação deve ser uma instância válida de Rating."
    )
    INVALID_REVIEWS_COUNT = "O total de resenhas deve ser um número inteiro."
    INVALID_RATINGS_COUNT = "O total de avaliações deve ser um número inteiro."
