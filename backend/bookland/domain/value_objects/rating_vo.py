from bookland.domain.exceptions import InvalidRatingException
from bookland.domain.errors import RatingErrors

MIN_RATING = 1.0
MAX_RATING = 5.0


class Rating:
    """
    Value Object que representa uma avaliação no sistema.
    Garante que:
    - O valor esteja entre 1.0 e 5.0
    - Pode ser None (avaliação ausente)
    - Se for média, deve ser float
    - Se for avaliação individual, deve ser int
    """

    def __init__(self, value: int | float | None = None, is_average: bool = False):
        self._validate(value, is_average)
        self._value = value

    def _validate(self, value: int | float | None, is_average: bool) -> None:
        if value is None:
            return

        if is_average and not isinstance(value, float):
            raise InvalidRatingException(RatingErrors.INVALID_TYPE_FLOAT)

        if not is_average and not isinstance(value, int):
            raise InvalidRatingException(RatingErrors.INVALID_TYPE_INT)

        if not (MIN_RATING <= value <= MAX_RATING):
            raise InvalidRatingException(
                RatingErrors.INTERVAL_INVALID.format(min=MIN_RATING, max=MAX_RATING)
            )

    @property
    def value(self) -> int | float | None:
        return self._value

    def is_empty(self) -> bool:
        return self.value is None

    def __str__(self):
        return str(self.value) if self.value is not None else "N/A"
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Rating) and self.value == other.value
