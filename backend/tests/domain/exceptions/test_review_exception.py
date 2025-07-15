import pytest
from bookland.domain.exceptions import ReviewNotFoundException


def test_review_not_found_exception_is_raised():
    with pytest.raises(ReviewNotFoundException) as exc_info:
        raise ReviewNotFoundException()

    assert str(exc_info.value) == "Resenha não foi encontrada."
