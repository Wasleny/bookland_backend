import re

from bookland.utils.text_utils import title_case
from bookland.domain.exceptions import InvalidLabelException
from bookland.domain.errors import LabelErrors

LABEL_MIN_LENGTH = 3
LABEL_MAX_LENGTH = 50
LABEL_PATTERN = r"^[A-Za-zÀ-ÿ0-9\s\-\']+$"


class Label:
    """
    Value Object que representa um rótulo (label) no sistema.
    Garante que o valor esteja no formato correto e com tamanho permitido.
    """

    def __init__(self, value: str):
        value = self._validate(value)
        self._value = value

    def _validate(self, value: str) -> str:
        if not isinstance(value, str):
            raise InvalidLabelException(LabelErrors.INVALID_TYPE)

        value = title_case(value.strip())

        if not LABEL_MIN_LENGTH <= len(value) <= LABEL_MAX_LENGTH:
            raise InvalidLabelException(
                LabelErrors.INVALID_LENGTH.format(
                    min=LABEL_MIN_LENGTH, max=LABEL_MAX_LENGTH
                )
            )

        if not re.fullmatch(LABEL_PATTERN, value):
            raise InvalidLabelException(LabelErrors.INVALID_FORMAT)

        return value

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        return isinstance(other, Label) and self.value == other.value

    def __str__(self) -> str:
        return self.value
