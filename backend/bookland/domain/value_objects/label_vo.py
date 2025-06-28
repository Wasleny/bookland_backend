import re
from bookland.utils.text_utils import title_case


class Label:
    def __init__(self, value: str):
        value = title_case(value.strip())
        self._is_valid(value)

        self._value = value

    def _is_valid(self, value: str) -> None:
        if not value:
            raise ValueError("Label deve ter tamanho maior que zero.")

        if len(value) > 50:
            raise ValueError("Label deve ter tamanho menor que 50 caracteres")

        if not re.fullmatch(r"^[A-Za-zÀ-ÿ0-9\s\-]+$", value):
            raise ValueError("Label deve estar dentro do formato correto")

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other_label) -> bool:
        return isinstance(other_label, Label) and self.value == other_label.value

    def __str__(self) -> str:
        return self.value
