REVIEW_NOT_FOUND = "Resenha não foi encontrada."


class InvalidReviewException(Exception): ...


class ReviewNotFoundException(Exception):
    def __init__(self, message=REVIEW_NOT_FOUND):
        super().__init__(message)
