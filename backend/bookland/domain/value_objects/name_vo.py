import re

from bookland.domain.exceptions import InvalidNameException
from bookland.domain.errors import NameErrors

NAME_PATTERN = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+([\-'\. ]+[A-Za-zÀ-ÖØ-öø-ÿ]+)*$"


class Name:
    """
    Value Object que representa o nome de uma pessoa.
    Garante que o nome seja uma string válida e esteja em um formato aceitável.
    """

    def __init__(self, value: str):
        self._validate(value)
        self._value = value

    def _validate(self, value: str) -> None:
        if not isinstance(value, str):
            raise InvalidNameException(NameErrors.INVALID_TYPE)

        if re.fullmatch(NAME_PATTERN, value) is None:
            raise InvalidNameException(NameErrors.INVALID_FORMAT)

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        return isinstance(other, Name) and self.value == other.value

    def __str__(self) -> str:
        return self.value
