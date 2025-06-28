from datetime import datetime, timezone

from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository
from bookland.domain.enums.user_role import UserRole
from bookland.infra.mongo_models.user import UserDocument
from bookland.infra.mappers.user_mapper import UserMapper
from bookland.interfaces.api.security import verify_password


class MongoUserRepository(UserRepository):
    async def login(self, email: str, password: str) -> User | None:
        document = await UserDocument.find_one(UserDocument.email == email)

        if document and verify_password(password, document.password):
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
        document = await UserDocument.get(user.id)

        if not document:
            raise Exception("Usuário não encontrado.")

        document.role = UserRole.ADMIN
        document.updated_at = datetime.now(timezone.utc)
        await document.save()

        return UserMapper.to_domain(document)

    async def demote_from_admin(self, user: User) -> User | None:
        document = await UserDocument.get(user.id)

        if not document:
            raise Exception("Usuário não encontrado.")

        document.role = UserRole.USER
        document.updated_at = datetime.now(timezone.utc)
        await document.save()

        return UserMapper.to_domain(document)

    async def search(self, search_term: str) -> User | None:
        document = await UserDocument.find_one(UserDocument.email == search_term)

        return UserMapper.to_domain(document) if document else None

    async def get_by_id(self, user_id: str) -> User | None:
        document = await UserDocument.get(user_id)

        return UserMapper.to_domain(document) if document else None

    async def logout(self) -> None: ...

    async def get_current_user(self) -> User | None: ...

    async def set_current_user(self, user_id: str) -> None: ...
