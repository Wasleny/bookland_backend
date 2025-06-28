from bookland.domain.value_objects.name_vo import Name
from bookland.domain.exceptions.series_exception import InvalidSeriesException
from datetime import datetime


class Series:
    def __init__(self, id: str, name: Name):
        self._validate_name(name)

        self._id = id
        self._name = name
        self._deleted_at = None

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, Name):
            raise InvalidSeriesException("Nome deve ser uma instância de Name")

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
    def is_deleted(self):
        return self._deleted_at is not None

    @property
    def deleted_at(self):
        return self._deleted_at
