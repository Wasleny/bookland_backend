from datetime import date

from bookland.domain.exceptions import InvalidDateException
from bookland.domain.errors import DateErrors


class Date:
    """
    Value Object que representa datas genéricas no sistema.
    Garante que a data seja uma instância de datetime.date.
    """

    def __init__(self, value: date):
        self._validate(value)
        self._value = value

    def _validate(self, value) -> None:
        if not isinstance(value, date):
            raise InvalidDateException(DateErrors.INVALID_TYPE)

    @property
    def value(self) -> date:
        return self._value

    def is_future(self) -> bool:
        return self.value > date.today()

    def to_json(self):
        return self.value.isoformat()

    def __str__(self) -> str:
        return self.value.strftime("%d/%m/%Y")

    def __eq__(self, other) -> bool:
        if isinstance(other, Date):
            return self.value == other.value
        if isinstance(other, date):
            return self.value == other

        return False
