from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository
from bookland.domain.enums.user_role import UserRole
from bookland.infra.mongo_models.user import UserDocument
from bookland.infra.mappers.user_mapper import UserMapper
from bookland.interfaces.api.security import verify_password
from bookland.domain.value_objects import Email, Password
from bookland.infra.utils.dates_utils import datetime_now


class MongoUserRepository(UserRepository):
    async def login(self, email: Email, password: Password) -> User | None:
        document = await UserDocument.find_one(UserDocument.email == email.value)

        if document and verify_password(password.value, document.password):
            return UserMapper.to_domain(document)

        return None

    async def register(self, user: User) -> User:
        user_found = await UserDocument.find_one({"email": user.email.value})

        if user_found:
            raise Exception("E-mail já cadastrado no sistema.")

        document = UserMapper.to_document(user)
        await document.insert()

        return UserMapper.to_domain(document)

    async def promote_to_admin(self, user: User) -> User | None:
        document = await UserDocument.find_one({"_id": user.id, "deleted_at": None})

        if not document:
            raise Exception("Usuário não encontrado.")

        document.role = UserRole.ADMIN
        document.updated_at = datetime_now()
        await document.save()

        return UserMapper.to_domain(document)

    async def demote_from_admin(self, user: User) -> User | None:
        document = await UserDocument.find_one({"_id": user.id, "deleted_at": None})

        if not document:
            raise Exception("Usuário não encontrado.")

        document.role = UserRole.USER
        document.updated_at = datetime_now()
        await document.save()

        return UserMapper.to_domain(document)

    async def search(self, search_term: str) -> User | None:
        document = await UserDocument.find_one(
            {"email": search_term, "deleted_at": None}
        )

        return UserMapper.to_domain(document) if document else None

    async def get_by_id(self, user_id: str) -> User | None:
        document = await UserDocument.find_one({"_id": user_id, "deleted_at": None})

        return UserMapper.to_domain(document) if document else None

    async def logout(self) -> None: ...

    async def get_current_user(self) -> User | None: ...

    async def set_current_user(self, user_id: str) -> None: ...
