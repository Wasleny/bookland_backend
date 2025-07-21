from bookland.domain.entities import User
from bookland.domain.repositories import UserRepository
from bookland.domain.enums import UserRole
from bookland.domain.value_objects import Email, Password
from bookland.domain.exceptions import (
    EmailAlreadyExistsException,
    UserNotFoundException,
)

from bookland.infra.mongo_models import UserDocument
from bookland.infra.mappers import UserMapper
from bookland.infra.utils.dates_utils import datetime_now

from bookland.interfaces.api.security import verify_password


class MongoUserRepository(UserRepository):
    async def login(self, email: Email, password: Password) -> User | None:
        document = await UserDocument.find_one(UserDocument.email == email.value)

        if document and verify_password(password.value, document.password):
            return UserMapper.to_domain(document)

        return None

    async def register(self, user: User) -> User:
        user_found = await UserDocument.find_one({"email": user.email.value})

        if user_found:
            raise EmailAlreadyExistsException()

        document = UserMapper.to_document(user)
        await document.insert()

        return UserMapper.to_domain(document)

    async def promote_to_admin(self, user_id: str) -> User | None:
        document = await UserDocument.find_one({"_id": user_id, "deleted_at": None})

        if not document:
            raise UserNotFoundException()

        document.role = UserRole.ADMIN
        document.updated_at = datetime_now()
        await document.save()

        return UserMapper.to_domain(document)

    async def demote_from_admin(self, user_id: str) -> User | None:
        document = await UserDocument.find_one({"_id": user_id, "deleted_at": None})

        if not document:
            raise UserNotFoundException()

        document.role = UserRole.USER
        document.updated_at = datetime_now()
        await document.save()

        return UserMapper.to_domain(document)

    async def get_by_email(self, email: str) -> User | None:
        document = await UserDocument.find_one({"email": email, "deleted_at": None})

        return UserMapper.to_domain(document) if document else None

    async def get_by_id(self, user_id: str) -> User | None:
        document = await UserDocument.find_one({"_id": user_id, "deleted_at": None})

        return UserMapper.to_domain(document) if document else None

    async def get_by_role(self, role: UserRole) -> list[User]:
        documents = await UserDocument.find(
            {"role": role, "deleted_at": None}
        ).to_list()

        return [UserMapper.to_domain(document) for document in documents]

    async def logout(self) -> None:
        raise NotImplementedError("...")

    async def get_current_user(self) -> User | None:
        raise NotImplementedError("...")

    async def set_current_user(self, user_id: str) -> None:
        raise NotImplementedError("...")
