from bookland.domain.exceptions.reading_in_progress_exception import (
    InvalidReadingInProgressException,
)


class ReadingInProgress:
    def __init__(self, id: str, book_id: str, user_id: str, progress: int):
        self._validate(book_id, user_id, progress)

        self._id = id
        self._book_id = book_id
        self._user_id = user_id
        self._progress = progress

    @staticmethod
    def _validate(book_id, user_id, progress):
        ReadingInProgress._validate_book_id(book_id)
        ReadingInProgress._validate_user_id(user_id)
        ReadingInProgress._validate_progress(progress)

    @staticmethod
    def _validate_user_id(user_id):
        if not isinstance(user_id, str):
            raise InvalidReadingInProgressException("O id do usuário deve ser stringo")

        if len(user_id) < 1:
            raise InvalidReadingInProgressException(
                "O id do usuário deve ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_book_id(book_id):
        if not isinstance(book_id, str):
            raise InvalidReadingInProgressException("O id do livro deve ser string")

        if len(book_id) < 1:
            raise InvalidReadingInProgressException(
                "O id do livro deve ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_progress(progress):
        if not isinstance(progress, int):
            raise InvalidReadingInProgressException("O progresso deve ser inteiro")

        if not (0 <= progress <= 100):
            raise InvalidReadingInProgressException(
                "O progresso deve ser um valor entre 0 e 100"
            )

    @property
    def id(self):
        return self._id

    @property
    def user_id(self):
        return self._user_id

    @property
    def book_id(self):
        return self._book_id

    @property
    def progress(self):
        return self._progress
