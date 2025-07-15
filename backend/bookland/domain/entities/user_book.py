from bookland.domain.exceptions import InvalidUserBookException
from bookland.domain.errors import UserBookErrors, CommonErrors


class UserBook:
    """
    Entity que representa a relação entre um livro e um usuário no sistema.

    Inclui os seguintes campos:
    - ID
    - ID do livro
    - ID do usuário
    - ID da estante padrão
    """

    def __init__(self, id: str, book_id: str, user_id: str, default_bookshelf_id: str):
        self._validate(id, book_id, user_id, default_bookshelf_id)

        self._id = id
        self._book_id = book_id
        self._user_id = user_id
        self._default_bookshelf_id = default_bookshelf_id

    def _validate(self, id: str, book_id: str, user_id: str, default_bookshelf: str):
        if not isinstance(id, str) or len(id) == 0:
            raise InvalidUserBookException(CommonErrors.INVALID_ID)

        if not isinstance(user_id, str) or len(user_id) == 0:
            raise InvalidUserBookException(CommonErrors.INVALID_USER_ID)

        if not isinstance(book_id, str) or len(book_id) == 0:
            raise InvalidUserBookException(CommonErrors.INVALID_BOOK_ID)

        if not isinstance(default_bookshelf, str) or len(book_id) == 0:
            raise InvalidUserBookException(UserBookErrors.INVALID_DEFAULT_BOOKSHELF)

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
    def default_bookshelf_id(self):
        return self._default_bookshelf_id
