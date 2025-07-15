import re

from bookland.domain.exceptions import InvalidIsbnException
from bookland.domain.errors import IsbnErrors


class Isbn:
    """
    Value Object que representa o ISBN de um livro.
    Garante que o valor seja um ISBN válido (ISBN-10 ou ISBN-13).
    """

    def __init__(self, value: str):
        self._validate(value)
        self._value = value

    def _validate(self, value: str) -> None:
        if not self._validate_isbn10(value) and not self._validate_isbn13(value):
            raise InvalidIsbnException(IsbnErrors.INVALID_FORMAT)

    def _validate_isbn10(self, isbn: str) -> bool:
        isbn = re.sub(r"[^0-9X]", "", isbn.upper())

        if len(isbn) != 10:
            return False

        total = 0
        for i, char in enumerate(isbn):
            if char == "X":
                digit = 10 if i == 9 else -1
            else:
                digit = int(char)
            total += (i + 1) * digit

        return total % 11 == 0

    def _validate_isbn13(self, isbn: str) -> bool:
        isbn = re.sub(r"\D", "", isbn)
        if len(isbn) != 13:
            return False

        total = 0
        for i, char in enumerate(isbn):
            digit = int(char)
            total += digit if i % 2 == 0 else digit * 3
        return total % 10 == 0

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        return isinstance(other, Isbn) and self.value == other.value

    def __str__(self) -> str:
        return self.value
