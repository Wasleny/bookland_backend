from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from bookland.interfaces.api.security import decode_access_token
from bookland.domain.entities.user import User
from bookland.domain.enums.user_role import UserRole
from bookland.interfaces.api.exceptions.user_exceptions import *
from bookland.infra.repositories import MongoUserRepository

security = HTTPBearer(auto_error=False)

repository = MongoUserRepository()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> User:
    if credentials is None:
        raise unauthorized_exception("Token não fornecido.")

    token = credentials.credentials
    payload = decode_access_token(token)

    if payload is None or "sub" not in payload:
        raise unauthorized_exception("Token inválido ou expirado.")

    user = await repository.get_by_id(payload["sub"])

    if user is None:
        raise user_not_found_exception()

    return user


async def admin_required(current_user=Depends(get_current_user)):
    if current_user.role != UserRole.ADMIN:
        raise forbidden_exception("Acesso permitido apenas para admins.")


async def owner_required(resource_user_id: str, current_user=Depends(get_current_user)):
    if resource_user_id != current_user.id:
        raise forbidden_exception()
