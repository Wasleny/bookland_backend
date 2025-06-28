from datetime import date
from bookland.domain.exceptions.review_exception import InvalidReviewException
from bookland.domain.value_objects.reading_criteria_vo import ReadingCriteria
from bookland.domain.value_objects.date_vo import Date


class Review:
    def __init__(
        self,
        id: str,
        user_id: str,
        book_id: str,
        rating: int = None,
        body: str = None,
        spoiler: bool = None,
        start_date: Date = None,
        end_date: Date = None,
        most_recent_reading: bool = None,
        rating_composition_criteria: list[ReadingCriteria] = None,
        independent_rating_criteria: list[ReadingCriteria] = None,
    ):
        self._validate(
            user_id,
            book_id,
            rating,
            body,
            spoiler,
            start_date,
            end_date,
            most_recent_reading,
            rating_composition_criteria,
            independent_rating_criteria,
        )

        self._id = id
        self._user_id = user_id
        self._book_id = book_id
        self._rating = rating
        self._body = body
        self._spoiler = spoiler
        self._start_date = start_date
        self._end_date = end_date
        self._most_recent_reading = most_recent_reading
        self._rating_composition_criteria = rating_composition_criteria
        self._independent_rating_criteria = independent_rating_criteria
        self._created_at = Date(date.today())
        self._updated_at = None

    @staticmethod
    def _validate(
        user_id,
        book_id,
        rating,
        body,
        spoiler,
        start_date,
        end_date,
        most_recent_reading,
        rating_composition_criteria,
        independent_rating_criteria,
    ):
        Review._validate_user_id(user_id)
        Review._validate_book_id(book_id)
        Review._validate_rating(rating)
        Review._validate_body(body)
        Review._validate_spoiler(spoiler)
        Review._validate_start_date(start_date)
        Review._validate_end_date(end_date)
        Review._validate_most_recent_reading(most_recent_reading)
        Review._validate_rating_criteria(rating_composition_criteria)
        Review._validate_rating_criteria(independent_rating_criteria)

    @staticmethod
    def _validate_user_id(user_id):
        if not isinstance(user_id, str) or len(user_id) < 1:
            raise InvalidReviewException(
                "O id do usuário deve ser string e ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_book_id(book_id):
        if not isinstance(book_id, str) or len(book_id) < 1:
            raise InvalidReviewException(
                "O id do livro deve ser string e ter tamanho maior que zero"
            )

    @staticmethod
    def _validate_rating(rating):
        if rating is None:
            return

        if not isinstance(rating, int) or rating not in [1, 2, 3, 4, 5]:
            raise InvalidReviewException(
                "A avaliação do livro deve ser inteiro e ser 1, 2, 3, 4 ou 5"
            )

    @staticmethod
    def _validate_body(body):
        if body is None:
            return

        if not isinstance(body, str) or len(body) < 3:
            raise InvalidReviewException(
                "A resenha deve ser string e ter tamanho miníno de 3 caracteres"
            )

    @staticmethod
    def _validate_spoiler(spoiler):
        if spoiler is None:
            return

        if not isinstance(spoiler, bool):
            raise InvalidReviewException("Spoiler deve ser um boolean")

    @staticmethod
    def _validate_start_date(start_date):
        if start_date is None:
            return

        if not isinstance(start_date, Date):
            raise InvalidReviewException(
                "A data de início deve ser uma instância de Date"
            )

    @staticmethod
    def _validate_end_date(end_date):
        if end_date is None:
            return

        if not isinstance(end_date, Date):
            raise InvalidReviewException(
                "A data de início deve ser uma instância de Date"
            )

    @staticmethod
    def _validate_most_recent_reading(most_recent_reading):
        if most_recent_reading is None:
            return

        if not isinstance(most_recent_reading, bool):
            raise InvalidReviewException("A leitura mais recente deve ser um boolean")

    @staticmethod
    def _validate_rating_criteria(rating_criteria):
        if rating_criteria == None:
            return

        if not isinstance(rating_criteria, list):
            raise InvalidReviewException(
                "A lista de critérios de composição / independentes devem ser uma instância de list"
            )

        if len(rating_criteria) == 0:
            raise InvalidReviewException("A lista precisa ter pelo menos um elemento")

        for item in rating_criteria:
            if not isinstance(item, ReadingCriteria):
                raise InvalidReviewException(
                    "Cada critério com nota devem ser uma instância de ReadingCriteria"
                )

    @property
    def id(self):
        return self._id

    @property
    def user_id(self):
        return self._user_id

    @property
    def book_id(self):
        return self._book_id

    @property
    def rating(self):
        return self._rating

    @property
    def body(self):
        return self._body

    @property
    def spoiler(self):
        return self._spoiler

    @property
    def start_date(self):
        return None if self._start_date is None else self._start_date.value

    @property
    def end_date(self):
        return None if self._end_date is None else self._end_date.value

    @property
    def most_recent_reading(self):
        return self._most_recent_reading

    @property
    def rating_composition_criteria(self):
        return self._rating_composition_criteria

    @property
    def independent_rating_criteria(self):
        return self._independent_rating_criteria

    @property
    def created_at(self):
        return None if self._created_at is None else self._created_at.value

    @property
    def updated_at(self):
        return None if self._updated_at is None else self._updated_at.value
