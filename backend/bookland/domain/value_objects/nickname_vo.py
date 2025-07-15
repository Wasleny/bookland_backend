import re

from bookland.domain.exceptions import InvalidNicknameException
from bookland.domain.errors import NicknameErrors

NICKNAME_PATTERN = r"[a-z]+(?:_[a-z]+)*"


class Nickname:
    """
    Value Object que representa o apelido (nickname) de um usuário.
    Garante que o valor seja uma string contendo apenas letras minúsculas e underscores.
    """

    def __init__(self, value: str):
        self._validate(value)
        self._value = value

    def _validate(self, value: str) -> None:
        if not isinstance(value, str):
            raise InvalidNicknameException(NicknameErrors.INVALID_TYPE)

        if re.fullmatch(NICKNAME_PATTERN, value) is None:
            raise InvalidNicknameException(NicknameErrors.INVALID_FORMAT)

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        return isinstance(other, Nickname) and self.value == other.value

    def __str__(self) -> str:
        return self.value
