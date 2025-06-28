from datetime import date

from bookland.domain.entities.user import User
from bookland.domain.enums.user_gender import UserGender
from bookland.domain.enums.user_role import UserRole
from bookland.infra.mongo_models.user import UserDocument
from bookland.domain.value_objects.name_vo import Name
from bookland.domain.value_objects.nickname_vo import Nickname
from bookland.domain.value_objects.birthday_vo import Birthday
from bookland.domain.value_objects.email_vo import Email
from bookland.domain.value_objects.password_vo import Password


class UserMapper:
    @staticmethod
    def to_domain(document: UserDocument) -> User:
        return User(
            id=document.id,
            name=Name(document.name),
            nickname=Nickname(document.nickname),
            email=Email(document.email),
            password=Password(document.password),
            gender=document.gender,
            birthday=Birthday(document.birthday),
            avatar_url=document.avatar_url,
            role=document.role,
        )

    @staticmethod
    def to_document(user: User) -> UserDocument:
        return UserDocument(
            id=user.id,
            name=user.name.value,
            nickname=user.nickname.value,
            email=user.email.value,
            password=user.password.value,
            gender=user.gender,
            birthday=user.birthday.value,
            avatar_url=user.avatar_url,
            role=user.role,
        )
