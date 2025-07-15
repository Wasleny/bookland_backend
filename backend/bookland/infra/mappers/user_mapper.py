from bookland.domain.entities import User
from bookland.domain.enums import UserGender
from bookland.infra.mongo_models import UserDocument
from bookland.domain.value_objects import (
    Name,
    Nickname,
    BirthDate,
    Email,
    Password,
    Rating,
)


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
            birthdate=BirthDate(document.birthdate) if document.birthdate else None,
            avatar_url=document.avatar_url if document.avatar_url else None,
            role=document.role,
            ratings_count=document.ratings_count,
            average_rating=Rating(document.average_rating),
            reviews_count=document.reviews_count,
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
            birthdate=user.birthdate.value if user.birthdate else None,
            avatar_url=user.avatar_url,
            role=user.role,
            ratings_count=user.ratings_count,
            average_rating=user.average_rating.value,
            reviews_count=user.reviews_count,
        )
