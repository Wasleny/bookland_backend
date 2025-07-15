import pytest
from bookland.domain.exceptions import AuthorNotFoundException


def test_author_not_found_exception_is_raised():
    with pytest.raises(AuthorNotFoundException) as exc_info:
        raise AuthorNotFoundException()

    assert str(exc_info.value) == "Autor não foi encontrado."
