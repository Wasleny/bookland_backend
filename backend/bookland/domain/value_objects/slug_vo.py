import re
from bookland.utils.text_utils import title_case


class Slug:
    def __init__(self, value: str):
        self._is_valid(value)
        self._value = value

    def _is_valid(self, value: str) -> None:
        if not re.match(r"^(?=.*[a-z])[a-z0-9]+(-[a-z0-9]+)*$", value):
            raise ValueError("Formato de slug inválido.")

    @property
    def value(self) -> str:
        return self._value

    def __str__(self):
        return self.value
