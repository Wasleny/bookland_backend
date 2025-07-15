from .author_service import (
    get_all_authors_usecase,
    create_author_usecase,
    get_author_usecase,
    soft_delete_author_usecase,
    update_author_usecase,
)

from .book_service import (
    create_book_use_case,
    get_all_books_use_case,
    get_book_use_case,
    search_books_use_case,
    update_book_use_case,
    soft_delete_book_use_case,
)

from .bookshelf_service import get_all_bookshelves_use_case

from .criterion_service import (
    create_criterion_usecase,
    get_all_criteria_usecase,
    get_criterion_usecase,
    search_criteria_usecase,
    soft_delete_criterion_usecase,
    update_criterion_usecase,
)

from .genre_service import get_all_genres_usecase

from .reading_in_progress_service import (
    create_reading_in_progress_usecase,
    delete_reading_in_progress_usecase,
    get_reading_in_progress_by_id_usecase,
    get_reading_in_progress_by_user_and_book_usecase,
    get_reading_in_progress_by_user_usecase,
    update_reading_in_progress_usecase,
)

from .review_service import (
    delete_review_usecase,
    create_review_usecase,
    get_review_by_id_usecase,
    get_most_recent_review_reading_usecase,
    get_reviews_by_book_usecase,
    delete_all_reviews_for_user_and_book_usecase,
    get_reviews_by_user_and_book_usecase,
    update_review_usecase,
)

from .series_service import (
    create_series_usecase,
    get_all_series_usecase,
    get_series_usecase,
    soft_delete_series_usecase,
    update_series_usecase,
)

from .trope_service import get_all_tropes_usecase

from .user_book_service import (
    delete_user_book_usecase,
    get_user_book_by_user_and_book_usecase,
    get_user_book_by_user_usecase,
    create_user_book_usecase,
    get_user_books_by_id_usecase,
    update_user_book_usecase,
)

from .user_service import (
    login_user_usecase,
    register_user_usecase,
    get_user_by_id_usecase,
    demote_user_from_admin_usecase,
    promote_user_to_admin_usecase,
    get_user_by_email_usecase,
    get_users_by_role_usecase,
)
