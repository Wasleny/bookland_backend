class ReviewErrors:
    INVALID_REVIEW = "A resenha deve ser uma string com no mínimo 3 caracteres."
    INVALID_SPOILER = "O spoiler deve ser um valor booleano."
    INVALID_START_DATE = "A data de início deve ser uma instância válida de Date."
    INVALID_END_DATE = "A data de término deve ser uma instância válida de Date."
    INVALID_RATING = "A nota deve ser uma instância válida de Rating."
    INVALID_MOST_RECENT = "A leitura mais recente deve ser um valor booleano."
    INVALID_CRITERIA_LIST = "A lista de critérios de composição/independentes deve ser uma instância válida de list."
    EMPTY_CRITERIA_LIST = "A lista de critérios deve conter pelo menos um elemento."
    INVALID_CRITERIA_ITEM = (
        "Cada critério com nota deve ser uma instância válida de ReadingCriteria."
    )
