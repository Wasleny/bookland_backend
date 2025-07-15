import pytest
from bookland.domain.exceptions import SeriesNotFoundException

def test_series_not_found_exception_is_raised():
    with pytest.raises(SeriesNotFoundException) as exc_info:
        raise SeriesNotFoundException()

    assert str(exc_info.value) == "Série não foi encontrada."
