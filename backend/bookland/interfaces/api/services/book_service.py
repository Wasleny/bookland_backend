from bookland.infra.repositories import MongoBookRepository
from bookland.application.usecases import (
    CreateBookUseCase,
    GetBookByIdUseCase,
    GetAllBooksUseCase,
    UpdateBookUseCase,
    SoftDeleteBookUseCase,
    SearchBooksUseCase,
)

repository = MongoBookRepository()

create_book_use_case = CreateBookUseCase(repository)
get_book_use_case = GetBookByIdUseCase(repository)
get_all_books_use_case = GetAllBooksUseCase(repository)
update_book_use_case = UpdateBookUseCase(repository)
soft_delete_book_use_case = SoftDeleteBookUseCase(repository)
search_books_use_case = SearchBooksUseCase(repository)
