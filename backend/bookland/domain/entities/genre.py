from datetime import datetime

from bookland.domain.value_objects import Label, Slug
from bookland.domain.exceptions import InvalidGenreException
from bookland.domain.errors import CommonErrors


class Genre:
    """
    Entity que representa um gênero literário no sistema.

    Inclui os seguintes campos:
    - ID
    - nome
    - nome em português
    - slug
    - estado de exclusão lógica (soft delete)
    """

    def __init__(self, id: str, name: Label, name_pt_br: Label, slug: Slug):
        self._validate(id, name, name_pt_br, slug)

        self._id = id
        self._name = name
        self._name_pt_br = name_pt_br
        self._slug = slug
        self._deleted_at = None

    def _validate(self, id: str, name: Label, name_pt_br: Label, slug: Slug):
        if not isinstance(id, str) or len(id) == 0:
            raise InvalidGenreException(CommonErrors.INVALID_ID)

        if not isinstance(name, Label):
            raise InvalidGenreException(CommonErrors.INVALID_LABEL)

        if not isinstance(name_pt_br, Label):
            raise InvalidGenreException(CommonErrors.INVALID_LABEL_PT_BR)

        if not isinstance(slug, Slug):
            raise InvalidGenreException(CommonErrors.INVALID_SLUG)

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
    def name_pt_br(self):
        return self._name_pt_br

    @property
    def slug(self):
        return self._slug

    @property
    def is_deleted(self):
        return self._deleted_at is not None

    @property
    def deleted_at(self):
        return self._deleted_at
