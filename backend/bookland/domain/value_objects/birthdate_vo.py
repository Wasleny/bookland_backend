from datetime import date

from bookland.domain.value_objects.date_vo import Date
from bookland.domain.exceptions import InvalidBirthDateException
from bookland.domain.errors import BirthDateErrors

MAX_AGE = 130
MIN_AGE = 12


class BirthDate(Date):
    """
    Value Object que representa a data de nascimento de um usuário.
    Garante que a data não esteja no futuro e que a idade esteja entre 12 e 130 anos.
    """

    def __init__(self, value: date):
        super().__init__(value)
        self._validate_birthdate()

    def _validate_birthdate(self):
        if self.is_future():
            raise InvalidBirthDateException(BirthDateErrors.FUTURE_DATE)

        age = self.age()

        if age < MIN_AGE:
            raise InvalidBirthDateException(BirthDateErrors.MINIMUM_AGE)

        if age > MAX_AGE:
            raise InvalidBirthDateException(BirthDateErrors.INVALID_AGE)

    def age(self):
        today = date.today()
        years = today.year - self.value.year

        if (today.month, today.day) < (self.value.month, self.value.day):
            years -= 1

        return years
