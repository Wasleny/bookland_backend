from bookland.infra.repositories import MongoUserRepository
from bookland.application.usecases import (
    DemoteUserFromAdminUseCase,
    PromoteUserToAdminUseCase,
    SearchUserUseCase,
    LoginUserUseCase,
    RegisterUserUseCase,
    GetUserByIdUseCase,
)

repository = MongoUserRepository()

register_user_usecase = RegisterUserUseCase(repository)
login_user_usecase = LoginUserUseCase(repository)
get_user_by_id_usecase = GetUserByIdUseCase(repository)
demote_user_from_admin_usecase = DemoteUserFromAdminUseCase(repository)
promote_user_to_admin_usecase = PromoteUserToAdminUseCase(repository)
search_user_usecase = SearchUserUseCase(repository)
