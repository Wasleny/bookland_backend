class ReadingCriteria:
    def __init__(self, criterion: str, rating: int):
        self._validate(criterion, rating)

        self._criterion = criterion
        self._rating = rating

    @staticmethod
    def _validate(criterion, rating):
        ReadingCriteria._validate_criterion(criterion)
        ReadingCriteria._validate_rating(rating)

    @staticmethod
    def _validate_criterion(criterion):
        if not isinstance(criterion, str) or len(criterion) < 3:
            raise ValueError("Critério deve ser string e ter no miníno 3 caracteres")

    @staticmethod
    def _validate_rating(rating):
        if not isinstance(rating, int) or rating not in [1, 2, 3, 4, 5]:
            raise ValueError("Nota deve ser inteiro e ser igual a 1, 2, 3, 4 ou 5")

    @property
    def criterion(self):
        return self._criterion

    @property
    def rating(self):
        return self._rating

    def to_dict(self):
        return {"criterion": self._criterion, "rating": self._rating}

    def __str__(self):
        return f"{self._criterion}: {self._rating}"

    def __eq__(self, other_reading_criteria):
        return (
            isinstance(other_reading_criteria, ReadingCriteria)
            and self.criterion == other_reading_criteria.criterion
            and self.rating == other_reading_criteria.rating
        )
