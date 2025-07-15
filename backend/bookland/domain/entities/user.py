from bookland.domain.value_objects import (
    Name,
    Nickname,
    Email,
    Password,
    BirthDate,
    Rating,
)
from bookland.domain.enums import UserRole, UserGender
from bookland.domain.exceptions import InvalidUserException
from bookland.domain.errors import UserErrors, CommonErrors


class User:
    """
    Entity que representa um usuário no sistema.

    Inclui os seguintes campos:
    - ID
    - nome
    - nickname
    - e-mail
    - senha
    - gênero
    - data de nascimento
    """

    def __init__(
        self,
        id: str,
        name: Name,
        nickname: Nickname,
        email: Email,
        password: Password,
        gender: UserGender,
        birthdate: BirthDate | None,
        avatar_url: str | None,
        role: UserRole,
        ratings_count: int = 0,
        average_rating: Rating = Rating(None),
        reviews_count: int = 0,
    ):
        self._validate(
            id,
            role,
            name,
            nickname,
            email,
            password,
            gender,
            birthdate,
            ratings_count,
            average_rating,
            reviews_count,
        )

        self._id = id
        self._name = name
        self._nickname = nickname
        self._email = email
        self._password = password
        self._gender = gender
        self._birthdate = birthdate
        self._ratings_count = ratings_count
        self._average_rating = average_rating
        self._reviews_count = reviews_count
        self._avatar_url = avatar_url
        self._role = role

    def _validate(
        self,
        id: str,
        role: UserRole,
        name: Name,
        nickname: Nickname,
        email: Email,
        password: Password,
        gender: UserGender,
        birthdate: BirthDate | None,
        ratings_count: int,
        average_rating: Rating,
        reviews_count: int,
    ) -> None:
        if not isinstance(id, str) or len(id) == 0:
            raise InvalidUserException(CommonErrors.INVALID_ID)

        if not isinstance(role, UserRole):
            raise InvalidUserException(UserErrors.INVALID_ROLE)

        if not isinstance(name, Name):
            raise InvalidUserException(CommonErrors.INVALID_NAME)

        if not isinstance(nickname, Nickname):
            raise InvalidUserException(UserErrors.INVALID_NICKNAME)

        if not isinstance(email, Email):
            raise InvalidUserException(UserErrors.INVALID_EMAIL)

        if not isinstance(password, Password):
            raise InvalidUserException(UserErrors.INVALID_PASSWORD)

        if not isinstance(gender, UserGender):
            raise InvalidUserException(UserErrors.INVALID_GENDER)

        if not isinstance(birthdate, BirthDate) and birthdate is not None:
            raise InvalidUserException(UserErrors.INVALID_BIRTHDATE)

        if not isinstance(average_rating, Rating):
            raise InvalidUserException(CommonErrors.INVALID_AVERAGE_RATING)

        if not isinstance(reviews_count, int):
            raise InvalidUserException(CommonErrors.INVALID_REVIEWS_COUNT)

        if not isinstance(ratings_count, int):
            raise InvalidUserException(CommonErrors.INVALID_RATINGS_COUNT)

    def promote_to_admin(self):
        if self.role == UserRole.USER:
            self._role = UserRole.ADMIN

    def demote_from_admin(self):
        if self.role == UserRole.ADMIN:
            self._role = UserRole.USER

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def nickname(self):
        return self._nickname

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def gender(self):
        return self._gender

    @property
    def birthdate(self):
        return self._birthdate

    @property
    def ratings_count(self):
        return self._ratings_count

    @property
    def average_rating(self):
        return self._average_rating

    @property
    def reviews_count(self):
        return self._reviews_count

    @property
    def avatar_url(self):
        return self._avatar_url

    @property
    def role(self):
        return self._role
