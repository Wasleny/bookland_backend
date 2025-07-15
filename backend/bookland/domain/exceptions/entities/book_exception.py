BOOK_NOT_FOUND = "Livro não foi encontrado."


class InvalidBookException(Exception): ...


class BookNotFoundException(Exception):
    def __init__(self, message=BOOK_NOT_FOUND):
        super().__init__(message)
