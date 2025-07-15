AUTHOR_NOT_FOUND = "Autor não foi encontrado."


class InvalidAuthorException(Exception): ...


class AuthorNotFoundException(Exception):
    def __init__(self, message=AUTHOR_NOT_FOUND):
        super().__init__(message)
