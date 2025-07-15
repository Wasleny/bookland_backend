import pytest
from bookland.domain.exceptions import UserBookNotFoundException

def test_user_book_not_found_exception_is_raised():
    with pytest.raises(UserBookNotFoundException) as exc_info:
        raise UserBookNotFoundException()

    assert str(exc_info.value) == "Relação usuário-livro não foi encontrada."
