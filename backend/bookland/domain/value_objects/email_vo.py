import re

class Email:
    def __init__(self, email: str):
        if not self.is_valid(email):
            raise ValueError(f"E-mail inválido")
        self._value = email

    def is_valid(self, email: str) -> bool:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        return re.match(pattern, email) is not None

    @property
    def value(self) -> str:
        return self._value
    
    def __eq__(self, other_email) -> bool:
        return isinstance(other_email, Email) and self._value == other_email.value
    
    def __str__(self) -> str:
        return self._value