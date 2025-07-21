from fastapi import Depends

from bookland.infra.repositories import MongoUserRepository
from bookland.application.usecases import (
    DemoteUserFromAdminUseCase,
    PromoteUserToAdminUseCase,
    GetUserByEmailUseCase,
    LoginUserUseCase,
    RegisterUserUseCase,
    GetUserByIdUseCase,
    GetUsersByRoleUseCase,
)


def get_user_repository() -> MongoUserRepository:
    return MongoUserRepository()


def get_register_user_usecase(
    repository: MongoUserRepository = Depends(get_user_repository),
) -> RegisterUserUseCase:
    return RegisterUserUseCase(repository)


def get_login_user_usecase(
    repository: MongoUserRepository = Depends(get_user_repository),
) -> LoginUserUseCase:
    return LoginUserUseCase(repository)


def get_get_user_by_id_usecase(
    repository: MongoUserRepository = Depends(get_user_repository),
) -> GetUserByIdUseCase:
    return GetUserByIdUseCase(repository)


def get_demote_user_from_admin_usecase(
    repository: MongoUserRepository = Depends(get_user_repository),
) -> DemoteUserFromAdminUseCase:
    return DemoteUserFromAdminUseCase(repository)


def get_promote_user_to_admin_usecase(
    repository: MongoUserRepository = Depends(get_user_repository),
) -> PromoteUserToAdminUseCase:
    return PromoteUserToAdminUseCase(repository)


def get_get_user_by_email_usecase(
    repository: MongoUserRepository = Depends(get_user_repository),
) -> GetUserByEmailUseCase:
    return GetUserByEmailUseCase(repository)


def get_get_users_by_role_usecase(
    repository: MongoUserRepository = Depends(get_user_repository),
) -> GetUsersByRoleUseCase:
    return GetUsersByRoleUseCase(repository)
