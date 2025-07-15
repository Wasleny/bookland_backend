from datetime import datetime

from bookland.domain.value_objects import Name
from bookland.domain.exceptions import InvalidAuthorException
from bookland.domain.errors import AuthorErrors, CommonErrors


class Author:
    """
    Entity que representa um autor(a) no sistema.

    Inclui os seguintes campos:
    - ID
    - nome
    - nacionalidade
    - estado de exclusão lógica (soft delete)
    """

    def __init__(self, id: str, name: Name, nationality: str | None = None):
        self._validate(id, name, nationality)

        self._id = id
        self._name = name
        self._nationality = nationality
        self._deleted_at = None

    def _validate(self, id: str, name: Name, nationality: str | None) -> None:
        if not isinstance(id, str):
            raise InvalidAuthorException(CommonErrors.INVALID_ID)

        if not isinstance(name, Name):
            raise InvalidAuthorException(CommonErrors.INVALID_NAME)

        if nationality is not None and not isinstance(nationality, str):
            raise InvalidAuthorException(AuthorErrors.INVALID_NATIONALITY)

    def soft_delete(self):
        if not self.is_deleted:
            self._deleted_at = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def nationality(self):
        return self._nationality

    @property
    def is_deleted(self):
        return self._deleted_at is not None

    @property
    def deleted_at(self):
        return self._deleted_at
