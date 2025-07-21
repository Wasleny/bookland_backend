from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from bookland.domain.repositories import UserRepository
from bookland.domain.entities.user import User
from bookland.domain.enums.user_role import UserRole
from bookland.interfaces.api.security import decode_access_token
from bookland.interfaces.api.exceptions.user_exceptions import *
from bookland.interfaces.api.services import get_user_repository

TOKEN_NOT_PROVIDED = "Token não fornecido."
INVALID_TOKEN = "Token inválido ou expirado."
ADMIN_ACESS_REQUIRED = "Acesso permitido apenas para admins."

security = HTTPBearer(auto_error=False)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    repository: UserRepository = Depends(get_user_repository),
) -> User:
    if credentials is None:
        raise unauthorized_exception(TOKEN_NOT_PROVIDED)

    token = credentials.credentials
    payload = decode_access_token(token)

    if payload is None or "sub" not in payload:
        raise unauthorized_exception(INVALID_TOKEN)

    user = await repository.get_by_id(payload["sub"])

    if user is None:
        raise user_not_found_exception()

    return user


async def admin_required(current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.ADMIN:
        raise forbidden_exception(ADMIN_ACESS_REQUIRED)


async def owner_required(
    resource_user_id: str, current_user: User = Depends(get_current_user)
):
    if resource_user_id != current_user.id:
        raise forbidden_exception()
