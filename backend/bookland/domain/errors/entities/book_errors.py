class BookErrors:
    INVALID_TITLE = "O título do livro deve ser uma instância válida de Title."
    INVALID_ORIGINAL_TITLE = "O título original deve ser uma instância válida de Title."
    INVALID_ISBN = "O ISBN deve ser uma instância válida de Isbn."
    INVALID_ASIN = "O ASIN deve ser uma string com exatamente 10 caracteres."
    INVALID_PUBLISHER = "A editora deve ser uma string não vazia."
    INVALID_BOOK_NUMBER = "O número do livro deve ser um float maior que zero."
    INVALID_ORIGINAL_SERIES_ID = "O ID da série original deve ser uma string não vazia."
    INVALID_SERIES_ID = "O ID da série deve ser uma string não vazia."
    INVALID_TROPES = "As tropes devem ser uma lista não vazia."
    INVALID_SECONDARY_GENRES = "Os gêneros secundários devem ser uma lista não vazia."
    INVALID_GENRE = "O gênero principal deve ser uma string não vazia."
    INVALID_LANGUAGE = "O idioma deve ser uma string não vazia."
    INVALID_PUBLICATION_DATE = (
        "A data de publicação deve ser uma instância válida de Date."
    )
    INVALID_PAGE_COUNT = "A quantidade de páginas deve ser um inteiro."
    INVALID_FORMAT = "O formato deve ser um dos valores definidos em BookFormat."
    INVALID_SYNOPSIS = "A sinopse deve ser uma string não vazia."
    INVALID_AUTHORS = "Os autores devem ser uma lista não vazia."
    INVALID_COVER = "A capa deve ser uma string não vazia."
    INVALID_ALTERNATIVE_EDITIONS = (
        "As edições alternativas devem ser uma lista não vazia."
    )
