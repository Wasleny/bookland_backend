from datetime import datetime

from bookland.domain.value_objects import Title, Slug
from bookland.domain.exceptions import InvalidSeriesException
from bookland.domain.errors import CommonErrors


class Series:
    """
    Entity que representa uma série no sistema.

    Inclui os seguintes campos:
    - ID
    - nome
    - slug
    - descrição
    - estado de exclusão lógica (soft delete)
    """

    def __init__(self, id: str, name: Title, slug: Slug, description: str):
        self._validate(id, name, slug, description)

        self._id = id
        self._name = name
        self._slug = slug
        self._description = description
        self._deleted_at = None

    @staticmethod
    def _validate(id: str, name: Title, slug: Slug, description: str) -> None:
        if not isinstance(id, str) or len(id) == 0:
            raise InvalidSeriesException(CommonErrors.INVALID_ID)

        if not isinstance(name, Title):
            raise InvalidSeriesException(CommonErrors.INVALID_TITLE)

        if not isinstance(slug, Slug):
            raise InvalidSeriesException(CommonErrors.INVALID_SLUG)

        if not isinstance(description, str) or len(description) == 0:
            raise InvalidSeriesException(CommonErrors.INVALID_DESCRIPTION)

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
    def slug(self):
        return self._slug

    @property
    def is_deleted(self):
        return self._deleted_at is not None

    @property
    def deleted_at(self):
        return self._deleted_at

    @property
    def description(self):
        return self._description
