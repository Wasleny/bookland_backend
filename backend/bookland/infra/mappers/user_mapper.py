from bookland.domain.entities import User
from bookland.domain.enums import UserGender
from bookland.infra.mongo_models import UserDocument
from bookland.domain.value_objects import Name, Nickname, Birthday, Email, Password


class UserMapper:
    @staticmethod
    def to_domain(document: UserDocument) -> User:
        return User(
            id=document.id,
            name=Name(document.name),
            nickname=Nickname(document.nickname),
            email=Email(document.email),
            password=Password(document.password),
            gender=document.gender if document.gender else UserGender.UNSPECIFIED,
            birthday=Birthday(document.birthday) if document.birthday else None,
            avatar_url=document.avatar_url if document.avatar_url else None,
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
            birthday=user.birthday.value if user.birthday else None,
            avatar_url=user.avatar_url,
            role=user.role,
        )
