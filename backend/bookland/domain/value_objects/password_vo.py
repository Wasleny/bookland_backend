import string

from bookland.domain.exceptions import InvalidPasswordException
from bookland.domain.errors import PasswordErrors


class Password:
    """
    Value Object que representa a senha de um usuário.
    Garante que a senha tenha no mínimo:
    - 8 caracteres
    - 1 letra minúscula
    - 1 letra maiúscula
    - 1 número
    - 1 caractere especial
    """

    def __init__(self, value: str):
        self._validate(value)
        self._value = value

    def _validate(self, password: str) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(PasswordErrors.REQUIRE_MIN_LENGTH)

        if not any(c.isupper() for c in password):
            raise InvalidPasswordException(PasswordErrors.REQUIRE_UPPERCASE)

        if not any(c.islower() for c in password):
            raise InvalidPasswordException(PasswordErrors.REQUIRE_LOWERCASE)

        if not any(c.isdigit() for c in password):
            raise InvalidPasswordException(PasswordErrors.REQUIRE_DIGIT)

        if not any(c in string.punctuation for c in password):
            raise InvalidPasswordException(PasswordErrors.REQUIRE_SPECIAL_CHAR)

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        return isinstance(other, Password) and self._value == other._value

    def __str__(self) -> str:
        return "*" * 8
