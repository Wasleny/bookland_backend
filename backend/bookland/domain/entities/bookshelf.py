from bookland.domain.value_objects import Label, Slug
from bookland.domain.exceptions import InvalidBookshelfException
from bookland.domain.errors import CommonErrors


class Bookshelf:
    """
    Entity que representa uma estante no sistema.

    Inclui os seguintes campos:
    - ID
    - nome
    - slug
    """

    def __init__(self, id: str, name: Label, slug: Slug):
        self._validate(id, name, slug)

        self._id = id
        self._name = name
        self._slug = slug

    def _validate(self, id: str, name: Label, slug: Slug):
        if not isinstance(id, str) or len(id) == 0:
            raise InvalidBookshelfException(CommonErrors.INVALID_ID)

        if not isinstance(name, Label):
            raise InvalidBookshelfException(CommonErrors.INVALID_LABEL)

        if not isinstance(slug, Slug):
            raise InvalidBookshelfException(CommonErrors.INVALID_SLUG)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def slug(self):
        return self._slug
