from bookland.domain.value_objects.label_vo import Label
from bookland.domain.exceptions.user_book_exception import InvalidUserBookException


class UserBook:
    def __init__(self, id: str, book_id: str, user_id: str, default_bookshelf: Label):
        self._validate(book_id, user_id, default_bookshelf)

        self._id = id
        self._book_id = book_id
        self._user_id = user_id
        self._default_bookshelf = default_bookshelf

    @staticmethod
    def _validate(book_id, user_id, default_bookshelf):
        UserBook._validate_book_id(book_id)
        UserBook._validate_user_id(user_id)
        UserBook._validate_default_bookshelf(default_bookshelf)

    @staticmethod
    def _validate_user_id(user_id):
        if not isinstance(user_id, str) or len(user_id) < 1:
            raise InvalidUserBookException(
                "O id do usuário deve ser string e ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_book_id(book_id):
        if not isinstance(book_id, str) or len(book_id) < 1:
            raise InvalidUserBookException(
                "O id do livro deve ser string e ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_default_bookshelf(default_bookshelf):
        if not isinstance(default_bookshelf, Label) or len(default_bookshelf.value) < 1:
            raise InvalidUserBookException(
                "A bookshelf padrão deve ser uma instância de Label e ter tamanho maior que zero"
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
    def default_bookshelf(self):
        return self._default_bookshelf
