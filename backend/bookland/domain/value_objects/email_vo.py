import re

from bookland.domain.exceptions import InvalidEmailException
from bookland.domain.errors import EmailErrors

EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


class Email:
    """
    Value Object que representa o e-mail de um usuário.
    Garante que o e-mail esteja em um formato válido.
    """

    def __init__(self, email: str):
        self._validate(email)
        self._value = email

    def _validate(self, email: str) -> None:
        if re.fullmatch(EMAIL_PATTERN, email) is None:
            raise InvalidEmailException(EmailErrors.INVALID_FORMAT)

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        return isinstance(other, Email) and self._value == other.value

    def __str__(self) -> str:
        return self._value
