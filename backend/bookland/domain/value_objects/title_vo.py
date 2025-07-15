import re

from bookland.domain.exceptions import InvalidTitleException
from bookland.domain.errors import TitleErrors

TITLE_PATTERN = r"[A-Za-zÀ-ÖØ-öø-ÿ0-9\s\.,:;!\?\'\"\-\(\)&]+"
TITLE_MIN_LENGTH = 1
TITLE_MAX_LENGTH = 150


class Title:
    """
    Value Object que representa um título genérico.
    Garante que o valor seja uma string válida dentro do formato e tamanho permitido.
    """

    def __init__(self, value: str):
        value = self._validate(value)
        self._value = value

    def _validate(self, value: str) -> str:
        if not isinstance(value, str):
            raise InvalidTitleException(TitleErrors.INVALID_TYPE)

        value = value.strip()

        if not TITLE_MIN_LENGTH <= len(value) <= TITLE_MAX_LENGTH:
            raise InvalidTitleException(
                TitleErrors.INVALID_LENGTH.format(
                    min=TITLE_MIN_LENGTH, max=TITLE_MAX_LENGTH
                )
            )

        if re.fullmatch(TITLE_PATTERN, value) is None:
            raise InvalidTitleException(TitleErrors.INVALID_FORMAT)

        return value

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        return isinstance(other, Title) and self.value == other.value

    def __str__(self) -> str:
        return self.value
