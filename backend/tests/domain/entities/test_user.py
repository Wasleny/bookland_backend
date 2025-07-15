import pytest
from datetime import date

from bookland.domain.value_objects import (
    Email,
    Password,
    Name,
    Nickname,
    BirthDate,
    Rating,
)
from bookland.domain.entities import User
from bookland.domain.enums import UserGender, UserRole
from bookland.domain.exceptions import InvalidUserException


def make_user_data(**overrides):
    base = {
        "id": "1",
        "name": Name("Test User"),
        "nickname": Nickname("test_user"),
        "email": Email("user@example.com"),
        "password": Password("uSer@1234"),
        "gender": UserGender.UNSPECIFIED,
        "birthdate": BirthDate(date(2002, 1, 1)),
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
    assert valid_user.password.value == "uSer@1234"
    assert valid_user.gender == "unspecified"
    assert valid_user.birthdate.value == date(2002, 1, 1)
    assert valid_user.ratings_count == 0
    assert valid_user.average_rating == Rating(None)
    assert valid_user.reviews_count == 0
    assert valid_user.avatar_url == ""
    assert valid_user.role == "user"


def test_invalid_role_should_raise_invalid_user_exception():
    with pytest.raises(InvalidUserException):
        User(**make_user_data(role="invalid_role"))


def test_invalid_name_should_raise_invalid_user_exception():
    with pytest.raises(InvalidUserException):
        User(**make_user_data(name="invalid_name"))


def test_invalid_average_rating_should_raise_invalid_user_exception():
    with pytest.raises(InvalidUserException):
        User(**make_user_data(average_rating="invalid_average_rating"))


def test_invalid_reviews_count_should_raise_invalid_user_exception():
    with pytest.raises(InvalidUserException):
        User(**make_user_data(reviews_count="invalid_reviews_count"))


def test_invalid_ratings_count_should_raise_invalid_user_exception():
    with pytest.raises(InvalidUserException):
        User(**make_user_data(ratings_count="invalid_ratings_count"))


def test_invalid_nickname_should_raise_invalid_user_exception():
    with pytest.raises(InvalidUserException):
        User(**make_user_data(nickname="invalid_nickname"))


def test_invalid_email_should_raise_invalid_user_exception():
    with pytest.raises(InvalidUserException):
        User(**make_user_data(email="invalid_email"))


def test_invalid_password_should_raise_invalid_user_exception():
    with pytest.raises(InvalidUserException):
        User(**make_user_data(password="invalid_password"))


def test_invalid_gender_should_raise_invalid_user_exception():
    with pytest.raises(InvalidUserException):
        User(**make_user_data(gender="invalid_gender"))


def test_invalid_birthdate_should_raise_invalid_user_exception():
    with pytest.raises(InvalidUserException):
        User(**make_user_data(birthdate="invalid_birthdate"))


def test_invalid_id_should_raise_invalid_user_exception():
    with pytest.raises(InvalidUserException):
        User(**make_user_data(id=1))


def test_promote_to_admin_successfully():
    valid_user = User(**make_user_data())

    assert valid_user.role == UserRole.USER

    valid_user.promote_to_admin()

    assert valid_user.role == UserRole.ADMIN


def test_demote_to_admin_successfully():
    valid_user = User(**make_user_data(role=UserRole.ADMIN))

    assert valid_user.role == UserRole.ADMIN

    valid_user.demote_from_admin()

    assert valid_user.role == UserRole.USER
