class Rating:
    def __init__(self, value: int | float | None = None, is_average: bool = False):
        self._is_valid(value, is_average)
        self._value = value

    def _is_valid(self, value: int | float | None, is_average: bool) -> None:
        if value is None:
            return

        if is_average and not (1.0 <= value <= 5.0):
            raise ValueError("A avaliação precisa ser entre 1.0 e 5.0")

        if not is_average and not (isinstance(value, int) and (1.0 <= value <= 5.0)):
            raise ValueError("A avaliação precisa ser um inteiro e estar entre 1 e 5")

    @property
    def value(self) -> int | float | None:
        return self._value

    def is_empty(self) -> bool:
        return self.value is None

    def __str__(self):
        return str(self.value) if self.value is not None else "N/A"
