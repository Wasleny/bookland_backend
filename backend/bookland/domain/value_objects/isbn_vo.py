import re


class Isbn:
    def __init__(self, value: str):
        self._is_valid(value)
        self._value = value

    def _is_valid(self, value: str) -> None:
        if not self._is_valid_isbn10(value) and not self._is_valid_isbn13(value):
            raise ValueError("ISBN não está no formato correto")

    def _is_valid_isbn10(self, isbn: str) -> bool:
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

    def _is_valid_isbn13(self, isbn: str) -> bool:
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

    def __eq__(self, other_isbn) -> bool:
        return isinstance(other_isbn, Isbn) and self.value == other_isbn.value

    def __str__(self) -> str:
        return self.value
