from bookland.domain.value_objects import Label, Rating
from bookland.domain.exceptions import InvalidReadingCriteriaException
from bookland.domain.errors import ReadingCriteriaErrors


class ReadingCriteria:
    """
    Value Object que representa um par de critério literário e nota.
    Garante que o critério seja do tipo Label e a nota do tipo Rating.
    """

    def __init__(self, criterion: Label, rating: Rating):
        self._validate(criterion, rating)
        self._criterion = criterion
        self._rating = rating

    def _validate(self, criterion: Label, rating: Rating) -> None:
        if not isinstance(rating, Rating) or not isinstance(rating.value, int):
            raise InvalidReadingCriteriaException(
                ReadingCriteriaErrors.RATING_INVALID_TYPE
            )

        if not isinstance(criterion, Label):
            raise InvalidReadingCriteriaException(
                ReadingCriteriaErrors.CRITERION_INVALID_TYPE
            )

    @property
    def criterion(self) -> str:
        return self._criterion.value

    @property
    def rating(self):
        return self._rating.value

    def to_dict(self) -> dict:
        return {"criterion": self.criterion, "rating": self.rating}

    def __str__(self) -> str:
        return f"{self.criterion}: {self.rating}"

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, ReadingCriteria)
            and self.criterion == other.criterion
            and self.rating == other.rating
        )
