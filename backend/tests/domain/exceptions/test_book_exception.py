import pytest
from bookland.domain.exceptions import BookNotFoundException

def test_book_not_found_exception_is_raised():
    with pytest.raises(BookNotFoundException) as exc_info:
        raise BookNotFoundException()

    assert str(exc_info.value) == "Livro não foi encontrado."
