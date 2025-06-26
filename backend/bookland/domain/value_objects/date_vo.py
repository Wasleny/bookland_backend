from datetime import date


class Date:
    def __init__(self, value: date):
        self._is_valid(value)
        self._value = value

    def _is_valid(self, value) -> None:
        if not isinstance(value, date):
            raise TypeError("Esperado uma instância de datetime.date")

    @property
    def value(self) -> date:
        return self._value

    def is_future(self) -> bool:
        return self.value > date.today()

    def __str__(self) -> str:
        return self.value.isoformat()

    def __eq__(self, other_date) -> bool:
        if isinstance(other_date, Date):
            return self.value == other_date.value
        if isinstance(other_date, date):
            return self.value == other_date

        return False
