import re

from bookland.domain.exceptions import InvalidSlugException
from bookland.domain.errors import SlugErrors

SLUG_PATTERN = r"^(?=.*[a-z])[a-z0-9]+(?:-[a-z0-9]+)*$"
SLUG_MIN_LENGTH = 3
SLUG_MAX_LENGTH = 50


class Slug:
    """
    Value Object que representa um slug genérico.
    Garante que o valor seja uma string em formato válido para URLs (lowercase, com hífens).
    """

    def __init__(self, value: str):
        self._validate(value)
        self._value = value

    def _validate(self, value: str) -> None:
        if not isinstance(value, str):
            raise InvalidSlugException(SlugErrors.INVALID_TYPE)

        if not SLUG_MIN_LENGTH <= len(value) <= SLUG_MAX_LENGTH:
            raise InvalidSlugException(
                SlugErrors.INVALID_LENGTH.format(
                    min=SLUG_MIN_LENGTH, max=SLUG_MAX_LENGTH
                )
            )

        if not re.fullmatch(SLUG_PATTERN, value):
            raise InvalidSlugException(SlugErrors.INVALID_FORMAT)

    @property
    def value(self) -> str:
        return self._value

    def __str__(self):
        return self.value

    def __eq__(self, other) -> bool:
        return isinstance(other, Slug) and self.value == other.value
