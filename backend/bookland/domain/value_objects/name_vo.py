import re


class Name:
    def __init__(self, value: str):
        self._is_valid(value)
        self._value = value

    def _is_valid(self, value: str) -> None:
        if re.fullmatch(r"^[A-Za-zÀ-ÖØ-öø-ÿ]+([\-'\. ]+[A-Za-zÀ-ÖØ-öø-ÿ]+)*$", value) is None:
            raise ValueError("Nome não está no formato correto")

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other_name) -> bool:
        return (
            isinstance(other_name, Name) and self.value == other_name.value
        )

    def __str__(self) -> str:
        return self.value
