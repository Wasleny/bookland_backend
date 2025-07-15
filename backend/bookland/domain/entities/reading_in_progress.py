from bookland.domain.exceptions import InvalidReadingInProgressException
from bookland.domain.errors import CommonErrors, ReadingInProgressErrors


class ReadingInProgress:
    """
    Entity que representa uma leitura em progresso no sistema.

    Inclui os seguintes campos:
    - ID
    - ID do usuário
    - ID do livro
    - progresso de leitura
    """

    def __init__(self, id: str, book_id: str, user_id: str, progress: int):
        self._validate(id, book_id, user_id, progress)

        self._id = id
        self._book_id = book_id
        self._user_id = user_id
        self._progress = progress

    def _validate(self, id: str, book_id: str, user_id: str, progress: int):
        if not isinstance(id, str) or len(id) == 0:
            raise InvalidReadingInProgressException(CommonErrors.INVALID_ID)

        if not isinstance(user_id, str) or len(user_id) == 0:
            raise InvalidReadingInProgressException(CommonErrors.INVALID_USER_ID)

        if not isinstance(book_id, str) or len(book_id) == 0:
            raise InvalidReadingInProgressException(CommonErrors.INVALID_BOOK_ID)

        if not isinstance(progress, int) or not (0 <= progress <= 100):
            raise InvalidReadingInProgressException(
                ReadingInProgressErrors.INVALID_PROGRESS
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
