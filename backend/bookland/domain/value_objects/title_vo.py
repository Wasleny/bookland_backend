import re


class Title:
    def __init__(self, value: str):
        value = value.strip()
        self._is_valid(value)
        self._value = value

    def _is_valid(self, value: str) -> None:
        if len(value) < 1:
            raise ValueError("Título não pode estar vazio.")

        if len(value) > 150:
            raise ValueError("Título não pode ter mais que 150 caracteres.")

        if re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9\s\.,:;!\?\'\"\-\(\)&]+", value) is None:
            raise ValueError("Título não está no formato correto")

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other_title) -> bool:
        return isinstance(other_title, Title) and self.value == other_title.value

    def __str__(self) -> str:
        return self.value
