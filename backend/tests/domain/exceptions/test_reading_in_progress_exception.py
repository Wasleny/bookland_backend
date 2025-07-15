import pytest
from bookland.domain.exceptions import ReadingInProgressNotFoundException


def test_reading_in_progress_not_found_exception_is_raised():
    with pytest.raises(ReadingInProgressNotFoundException) as exc_info:
        raise ReadingInProgressNotFoundException()

    assert str(exc_info.value) == "Leitura em andamento não foi encontrada."
