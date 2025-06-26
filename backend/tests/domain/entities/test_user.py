import pytest
from datetime import date
from bookland.domain.value_objects.email_vo import Email
from bookland.domain.value_objects.password_vo import Password
from bookland.domain.value_objects.name_vo import Name
from bookland.domain.value_objects.nickname_vo import Nickname
from bookland.domain.value_objects.birthday_vo import Birthday
from bookland.domain.entities.user import User
from bookland.domain.enums.user_gender import UserGender
from bookland.domain.enums.user_role import UserRole
from bookland.domain.exceptions.user_exception import InvalidUserException


def make_user_data(**overrides):
    base = {
        "id": "1",
        "name": Name("Test User"),
        "nickname": Nickname("test_user"),
        "email": Email("user@example.com"),
        "password": Password("user1234"),
        "gender": UserGender.UNSPECIFIED,
        "birthday": Birthday(date(2002, 1, 1)),
        "avatar_url": "",
        "role": UserRole.USER,
    }
    base.update(overrides)

    return base


def test_valid_user_should_be_created():
    valid_user = User(**make_user_data())

    assert valid_user.id == "1"
    assert valid_user.name.value == "Test User"
    assert valid_user.nickname.value == "test_user"
    assert valid_user.email.value == "user@example.com"
    assert valid_user.password.value == "user1234"
    assert valid_user.gender == "unspecified"
    assert valid_user.birthday.value == date(2002, 1, 1)
    assert valid_user.rating_count == 0
    assert valid_user.average_rating == 0
    assert valid_user.review_count == 0
    assert valid_user.avatar_url == ""
    assert valid_user.role == "user"


def test_invalid_role_should_raise_invalid_user_exception():
    invalid_user = make_user_data(role="invalid_role")

    with pytest.raises(InvalidUserException):
        User(**invalid_user)


def test_invalid_name_should_raise_invalid_user_exception():
    invalid_user = make_user_data(name="invalid_name")

    with pytest.raises(InvalidUserException):
        User(**invalid_user)


def test_invalid_nickname_should_raise_invalid_user_exception():
    invalid_user = make_user_data(nickname="invalid_nickname")

    with pytest.raises(InvalidUserException):
        User(**invalid_user)


def test_invalid_email_should_raise_invalid_user_exception():
    invalid_user = make_user_data(email="invalid_email")

    with pytest.raises(InvalidUserException):
        User(**invalid_user)


def test_invalid_password_should_raise_invalid_user_exception():
    invalid_user = make_user_data(password="invalid_password")

    with pytest.raises(InvalidUserException):
        User(**invalid_user)


def test_invalid_gender_should_raise_invalid_user_exception():
    invalid_user = make_user_data(gender="invalid_gender")

    with pytest.raises(InvalidUserException):
        User(**invalid_user)


def test_invalid_birthday_should_raise_invalid_user_exception():
    invalid_user = make_user_data(birthday="invalid_birthday")

    with pytest.raises(InvalidUserException):
        User(**invalid_user)


def test_promote_to_admin_successfully():
    valid_user = User(**make_user_data())

    assert valid_user.role == UserRole.USER

    valid_user.promote_to_admin()

    assert valid_user.role == UserRole.ADMIN


def test_demote_to_admin_successfully():
    valid_user = User(**make_user_data(role=UserRole.ADMIN))

    assert valid_user.role == UserRole.ADMIN

    valid_user.demote_to_admin()

    assert valid_user.role == UserRole.USER
