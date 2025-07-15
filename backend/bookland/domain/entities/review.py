from bookland.domain.exceptions import InvalidReviewException
from bookland.domain.value_objects import ReadingCriteria, Date, Rating
from bookland.domain.errors import ReviewErrors, CommonErrors


class Review:
    """
    Entity que representa uma resenha de livro no sistema.

    Inclui os seguintes campos:
    - ID
    - ID do usuário
    - ID do livro
    - indicação de spoiler
    - indicação de resenha mais recente do livro
    - nota atribuída
    - texto da resenha
    - data de início da leitura
    - data de término da leitura
    - lista de critérios de composição da nota
    - lista de critérios independentes avaliados
    """

    def __init__(
        self,
        id: str,
        user_id: str,
        book_id: str,
        spoiler: bool,
        most_recent_reading: bool,
        rating: Rating | None = None,
        body: str | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        rating_composition_criteria: list[ReadingCriteria] | None = None,
        independent_rating_criteria: list[ReadingCriteria] | None = None,
    ):
        self._validate(
            id,
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

    def _validate(
        self,
        id: str,
        user_id: str,
        book_id: str,
        rating: Rating | None,
        body: str | None,
        spoiler: bool,
        start_date: Date | None,
        end_date: Date | None,
        most_recent_reading: bool,
        rating_composition_criteria: list | None,
        independent_rating_criteria: list | None,
    ) -> None:
        if not isinstance(id, str) or len(id) == 0:
            raise InvalidReviewException(CommonErrors.INVALID_ID)

        if not isinstance(user_id, str) or len(user_id) == 0:
            raise InvalidReviewException(CommonErrors.INVALID_USER_ID)

        if not isinstance(book_id, str) or len(book_id) == 0:
            raise InvalidReviewException(CommonErrors.INVALID_BOOK_ID)

        if (
            not isinstance(rating, Rating)
            or not isinstance(rating.value, int)
            and not rating.is_empty()
        ):
            raise InvalidReviewException(ReviewErrors.INVALID_RATING)

        if body is not None and (not isinstance(body, str) or len(body) < 3):
            raise InvalidReviewException(ReviewErrors.INVALID_REVIEW)

        if not isinstance(spoiler, bool):
            raise InvalidReviewException(ReviewErrors.INVALID_SPOILER)

        if start_date is not None and not isinstance(start_date, Date):
            raise InvalidReviewException(ReviewErrors.INVALID_START_DATE)

        if end_date is not None and not isinstance(end_date, Date):
            raise InvalidReviewException(ReviewErrors.INVALID_END_DATE)

        if not isinstance(most_recent_reading, bool):
            raise InvalidReviewException(ReviewErrors.INVALID_MOST_RECENT)

        self._validate_rating_criteria(rating_composition_criteria)
        self._validate_rating_criteria(independent_rating_criteria)

    def _validate_rating_criteria(self, rating_criteria: list | None) -> None:
        if rating_criteria == None:
            return

        if not isinstance(rating_criteria, list):
            raise InvalidReviewException(ReviewErrors.INVALID_CRITERIA_LIST)

        if len(rating_criteria) == 0:
            raise InvalidReviewException(ReviewErrors.EMPTY_CRITERIA_LIST)

        for item in rating_criteria:
            if not isinstance(item, ReadingCriteria):
                raise InvalidReviewException(ReviewErrors.INVALID_CRITERIA_ITEM)

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
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def most_recent_reading(self):
        return self._most_recent_reading

    @property
    def rating_composition_criteria(self):
        return self._rating_composition_criteria

    @property
    def independent_rating_criteria(self):
        return self._independent_rating_criteria
