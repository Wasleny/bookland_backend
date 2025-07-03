from bookland.domain.value_objects.name_vo import Name
from bookland.domain.value_objects.nickname_vo import Nickname
from bookland.domain.value_objects.email_vo import Email
from bookland.domain.value_objects.password_vo import Password
from bookland.domain.value_objects.birthday_vo import Birthday
from bookland.domain.enums.user_role import UserRole
from bookland.domain.enums.user_gender import UserGender
from bookland.domain.exceptions.user_exception import InvalidUserException


class User:
    def __init__(
        self,
        id: str,
        name: Name,
        nickname: Nickname,
        email: Email,
        password: Password,
        gender: UserGender,
        birthday: Birthday | None,
        avatar_url: str | None,
        role: UserRole,
    ):

        self._validate_user(
            role,
            name,
            nickname,
            email,
            password,
            gender,
            birthday,
        )

        self._id = id
        self._name = name
        self._nickname = nickname
        self._email = email
        self._password = password
        self._gender = gender
        self._birthday = birthday
        self._rating_count = 0
        self._average_rating = 0
        self._review_count = 0
        self._avatar_url = avatar_url
        self._role = role

    @staticmethod
    def _validate_user(role, name, nickname, email, password, gender, birthday):
        User._validate_role(role)
        User._validate_name(name)
        User._validate_nickname(nickname)
        User._validate_email(email)
        User._validate_password(password)
        User._validate_gender(gender)
        User._validate_birthday(birthday)

    @staticmethod
    def _validate_role(role):
        if not isinstance(role, UserRole):
            raise InvalidUserException("Role deve ser um dos valores de UserRole")

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, Name):
            raise InvalidUserException("Nome deve ser uma instância de Name")

    @staticmethod
    def _validate_nickname(nickname):
        if not isinstance(nickname, Nickname):
            raise InvalidUserException("Nickname deve ser uma instância de Nickname")

    @staticmethod
    def _validate_email(email):
        if not isinstance(email, Email):
            raise InvalidUserException("Email deve ser uma instância de Email")

    @staticmethod
    def _validate_password(password):
        if not isinstance(password, Password):
            raise InvalidUserException("Senha deve ser uma instância de Password")

    @staticmethod
    def _validate_gender(gender):
        if not isinstance(gender, UserGender):
            raise InvalidUserException("Gênero deve ser um dos valores de UserGender")

    @staticmethod
    def _validate_birthday(birthday):
        if not isinstance(birthday, Birthday) and birthday is not None:
            raise InvalidUserException(
                "Data de nascimento deve ser uma instância de Birthday"
            )

    def promote_to_admin(self):
        if self.role == UserRole.USER:
            self._role = UserRole.ADMIN

    def demote_to_admin(self):
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
    def birthday(self):
        return self._birthday

    @property
    def rating_count(self):
        return self._rating_count

    @property
    def average_rating(self):
        return self._average_rating

    @property
    def review_count(self):
        return self._review_count

    @property
    def avatar_url(self):
        return self._avatar_url

    @property
    def role(self):
        return self._role
