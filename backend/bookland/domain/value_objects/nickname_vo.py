import re


class Nickname:
    def __init__(self, value: str):
        self._is_valid(value)
        self._value = value

    def _is_valid(self, value: str) -> None:
        if re.fullmatch(r"[a-z]+(?:_[a-z]+)*", value) is None:
            raise ValueError("Nickname não está no formato correto")

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other_nickname) -> bool:
        return (
            isinstance(other_nickname, Nickname) and self.value == other_nickname.value
        )

    def __str__(self) -> str:
        return self.value
