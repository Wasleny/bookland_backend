from bookland.domain.value_objects.label_vo import Label
from bookland.domain.exceptions.criterion_exception import InvalidCriterionException
from datetime import datetime


class Criterion:
    def __init__(self, id: str, name: Label, description: str, user_id: str):
        self._validate_criterion(name, description, user_id)

        self._id = id
        self._name = name
        self._description = description
        self._user_id = user_id
        self._deleted_at = None

    @staticmethod
    def _validate_criterion(name, description, user_id):
        Criterion._validate_name(name)
        Criterion._validate_description(description)
        Criterion._validate_user_id(user_id)

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, Label):
            raise InvalidCriterionException("Nome deve ser uma instância de Label")

    @staticmethod
    def _validate_description(description):
        if not isinstance(description, str) or len(description) < 1:
            raise InvalidCriterionException(
                "Descrição deve ter tamanho maior que zero e ser uma string"
            )

    @staticmethod
    def _validate_user_id(user_id):
        if not isinstance(user_id, str) or len(user_id) < 1:
            raise InvalidCriterionException(
                "Id do usuário deve ser uma string e deve existir"
            )

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
