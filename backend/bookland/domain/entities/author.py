from bookland.domain.value_objects.name_vo import Name
from bookland.domain.exceptions.author_exception import InvalidAuthorException
from datetime import datetime


class Author:
    def __init__(self, id: str, name: Name, nationality: str | None = None):
        self._validate_name(name)

        self._id = id
        self._name = name
        self._nationality = nationality
        self._deleted_at = None

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, Name):
            raise InvalidAuthorException("Nome deve ser uma instância de Name")

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
