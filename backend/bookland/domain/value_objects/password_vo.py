class Password:
    def __init__(self, value: str):
        if not self._is_valid(value):
            raise ValueError(
                "Senha precisa ter no mínino 8 caracteres e conter letras e números."
            )
        self._value = value

    def _is_valid(self, password: str) -> bool:
        return (
            len(password) >= 8
            and any(c.isalpha() for c in password)
            and any(c.isdigit() for c in password)
        )

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        return isinstance(other, Password) and self._value == other._value

    def __str__(self) -> str:
        return "*" * 8
