from .author_service import (
    get_all_authors_usecase,
    create_author_usecase,
    get_author_usecase,
    soft_delete_author_usecase,
    update_author_usecase,
)

from .user_service import (
    login_user_usecase,
    register_user_usecase,
    get_user_by_id_usecase,
    demote_user_from_admin_usecase,
    promote_user_to_admin_usecase,
    search_user_usecase,
)

from .criterion_service import (
    create_criterion_usecase,
    get_all_criteria_usecase,
    get_criterion_usecase,
    search_criteria_usecase,
    soft_delete_criterion_usecase,
    update_criterion_usecase,
)

from .genre_service import get_all_genres_usecase

from .trope_service import get_all_tropes_usecase