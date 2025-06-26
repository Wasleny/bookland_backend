from datetime import date
from .date_vo import Date


class Birthday(Date):
    def __init__(self, value: date):
        super().__init__(value)
        self._is_valid_birthday()

    def _is_valid_birthday(self):
        if self.is_future():
            raise ValueError("Data de nascimento não pode ser no futuro")

    def age(self):
        today = date.today()
        years = today.year - self.value.year

        if (today.month, today.day) < (self.value.month, self.value.day):
            years -= 1

        return years
