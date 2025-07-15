from uuid import uuid4
from datetime import date

from bookland.domain.value_objects import Email, Password, Name, Nickname, BirthDate
from bookland.domain.entities import User
from bookland.domain.enums import UserGender, UserRole


def create_user(**overrides) -> User:
    base = {
        "id": str(uuid4()),
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

    return User(**base)
