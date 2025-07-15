from datetime import datetime

from bookland.domain.value_objects import Label
from bookland.domain.exceptions import InvalidCriterionException
from bookland.domain.errors import CommonErrors


class Criterion:
    """
    Entity que representa um critério no sistema.

    Inclui os seguintes campos:
    - ID
    - nome
    - descrição
    - ID do usuário
    - estado de exclusão lógica (soft delete)
    """

    def __init__(self, id: str, name: Label, description: str, user_id: str):
        self._validate(id, name, description, user_id)

        self._id = id
        self._name = name
        self._description = description
        self._user_id = user_id
        self._deleted_at = None

    def _validate(self, id: str, name: Label, description: str, user_id: str):
        if not isinstance(id, str) or len(id) == 0:
            raise InvalidCriterionException(CommonErrors.INVALID_ID)

        if not isinstance(name, Label):
            raise InvalidCriterionException(CommonErrors.INVALID_LABEL)

        if not isinstance(description, str) or len(description) < 1:
            raise InvalidCriterionException(CommonErrors.INVALID_DESCRIPTION)

        if not isinstance(user_id, str) or len(user_id) == 0:
            raise InvalidCriterionException(CommonErrors.INVALID_USER_ID)

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
    def description(self):
        return self._description

    @property
    def user_id(self):
        return self._user_id

    @property
    def is_deleted(self):
        return self._deleted_at is not None

    @property
    def deleted_at(self):
        return self._deleted_at
