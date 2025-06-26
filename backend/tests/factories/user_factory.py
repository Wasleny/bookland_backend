from uuid import uuid4
from datetime import date
from bookland.domain.value_objects.email_vo import Email
from bookland.domain.value_objects.password_vo import Password
from bookland.domain.value_objects.name_vo import Name
from bookland.domain.value_objects.nickname_vo import Nickname
from bookland.domain.value_objects.birthday_vo import Birthday
from bookland.domain.entities.user import User
from bookland.domain.enums.user_gender import UserGender
from bookland.domain.enums.user_role import UserRole


def create_user(**overrides) -> User:
    base = {
        "id": str(uuid4()),
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

    return User(**base)
