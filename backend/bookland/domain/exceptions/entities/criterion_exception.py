CRITERION_NOT_FOUND = "Critério de avaliação não foi encontrado."


class InvalidCriterionException(Exception): ...


class CriterionNotFoundException(Exception):
    def __init__(self, message=CRITERION_NOT_FOUND):
        super().__init__(message)
