from .author_service import (
    get_author_repository,
    get_create_author_usecase,
    get_get_all_authors_usecase,
    get_get_author_usecase,
    get_soft_delete_author_usecase,
    get_update_author_usecase,
)

from .book_service import (
    get_book_repository,
    get_create_book_use_case,
    get_get_all_books_use_case,
    get_get_book_use_case,
    get_search_books_use_case,
    get_soft_delete_book_use_case,
    get_update_book_use_case,
)

from .bookshelf_service import (
    get_bookshelf_repository,
    get_get_all_bookshelves_use_case,
)

from .criterion_service import (
    get_criterion_repository,
    get_create_criterion_usecase,
    get_get_all_criteria_usecase,
    get_get_criterion_usecase,
    get_search_criteria_usecase,
    get_soft_delete_criterion_usecase,
    get_update_criterion_usecase,
)

from .genre_service import get_genre_repository, get_get_all_genres_usecase

from .reading_in_progress_service import (
    get_reading_in_progress_repository,
    get_get_reading_in_progress_by_user_usecase,
    get_create_reading_in_progress_usecase,
    get_update_reading_in_progress_usecase,
    get_delete_reading_in_progress_usecase,
    get_get_reading_in_progress_by_user_and_book_usecase,
    get_get_reading_in_progress_by_id_usecase,
)

from .review_service import (
    get_create_review_usecase,
    get_delete_all_reviews_for_user_and_book_usecase,
    get_delete_review_usecase,
    get_get_most_recent_review_reading_usecase,
    get_get_review_by_id_usecase,
    get_get_reviews_by_book_usecase,
    get_get_reviews_by_user_and_book_usecase,
    get_update_review_usecase,
    get_review_repository,
)

from .series_service import (
    get_create_series_usecase,
    get_get_all_series_usecase,
    get_get_series_usecase,
    get_soft_delete_series_usecase,
    get_series_repository,
    get_update_series_usecase,
)

from .trope_service import get_get_all_tropes_usecase, get_trope_repository

from .user_book_service import (
    get_get_user_book_by_user_and_book_usecase,
    get_create_user_book_usecase,
    get_delete_user_book_usecase,
    get_get_user_book_by_user_usecase,
    get_get_user_books_by_id_usecase,
    get_update_user_book_usecase,
    get_user_book_repository,
)

from .user_service import (
    get_register_user_usecase,
    get_demote_user_from_admin_usecase,
    get_get_user_by_email_usecase,
    get_get_user_by_id_usecase,
    get_get_users_by_role_usecase,
    get_login_user_usecase,
    get_promote_user_to_admin_usecase,
    get_user_repository,
)
