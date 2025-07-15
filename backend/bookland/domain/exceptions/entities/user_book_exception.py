USER_BOOK_NOT_FOUND = "Relação usuário-livro não foi encontrada."


class InvalidUserBookException(Exception): ...


class UserBookNotFoundException(Exception):
    def __init__(self, message=USER_BOOK_NOT_FOUND):
        super().__init__(message)
