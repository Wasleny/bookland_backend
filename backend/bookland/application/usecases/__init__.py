from .author.create_author import CreateAuthorUseCase
from .author.get_all_authors import GetAllAuthorsUseCase
from .author.get_author_by_id import GetAuthorByIdUseCase
from .author.soft_delete_author import SoftDeleteAuthorUseCase
from .author.update_author import UpdateAuthorUseCase


from .book.create_book import CreateBookUseCase
from .book.get_all_books import GetAllBooksUseCase
from .book.get_book_by_id import GetBookByIdUseCase
from .book.search_books import SearchBooksUseCase
from .book.soft_delete_book import SoftDeleteBookUseCase
from .book.update_book import UpdateBookUseCase


from .criterion.create_criterion import CreateCriterionUseCase
from .criterion.get_all_criteria import GetAllCriteriaUseCase
from .criterion.get_criterion_by_id import GetCriterionByIdUseCase
from .criterion.search_criteria import SearchCriteriaUseCase
from .criterion.soft_delete_criterion import SoftDeleteCriterionUseCase
from .criterion.update_criterion import UpdateCriterionUseCase


from .reading_in_progress.create_reading_in_progress import (
    CreateReadingInProgressUseCase,
)
from .reading_in_progress.delete_reading_in_progress import (
    DeleteReadingInProgressUseCase,
)
from .reading_in_progress.get_reading_in_progress_by_id import (
    GetReadingInProgressByIdUseCase,
)
from .reading_in_progress.get_reading_in_progress_by_user_and_book import (
    GetReadingInProgressByUserAndBookUseCase,
)
from .reading_in_progress.get_reading_in_progress_by_user import (
    GetReadingInProgressByUserUseCase,
)
from .reading_in_progress.update_reading_in_progress import (
    UpdateReadingInProgressUseCase,
)


from .review.create_review import CreateReviewUseCase
from .review.delete_all_reviews_for_user_and_book import (
    DeleteAllReviewsForUserAndBookUseCase,
)
from .review.delete_review import DeleteReviewUseCase
from .review.get_most_recent_review_reading import GetMostRecentReviewReadingUseCase
from .review.get_review_by_id import GetReviewByIdUseCase
from .review.get_review_by_user_and_book import GetReviewsByUserAndBookUseCase
from .review.get_reviews_by_book import GetReviewsByBookUseCase
from .review.update_review import UpdateReviewUseCase


from .series.create_series import CreateSeriesUseCase
from .series.get_all_series import GetAllSeriesUseCase
from .series.get_series_by_id import GetSeriesByIdUseCase
from .series.soft_delete_series import SoftDeleteSeriesUseCase
from .series.update_series import UpdateSeriesUseCase


from .user.demote_user_from_admin import DemoteUserFromAdminUseCase
from .user.get_current_user import GetCurrentUserUseCase
from .user.get_user_by_id import GetUserByIdUseCase
from .user.login_user import LoginUserUseCase
from .user.logout_user import LogoutUserUseCase
from .user.promote_user_to_admin import PromoteUserToAdminUseCase
from .user.register_user import RegisterUserUseCase
from .user.get_user_by_email import GetUserByEmailUseCase
from .user.set_current_user import SetCurrentUserUseCase
from .user.get_users_by_role import GetUserByRoleUseCase


from .user_book.create_user_book import CreateUserBookUseCase
from .user_book.delete_user_book import DeleteUserBookUseCase
from .user_book.get_user_book_by_id import GetUserBookByIdUseCase
from .user_book.get_user_book_by_user_and_book import GetUserBookByUserAndBookUseCase
from .user_book.get_user_book_by_user import GetUserBookByUserUseCase
from .user_book.update_user_book import UpdateUserBookUseCase


from .genre.get_all_genres import GetAllGenresUseCase

from .trope.get_all_tropes import GetAllTropesUseCase

from .bookshelf.get_all_bookshelves import GetAllBookshelvesUseCase
