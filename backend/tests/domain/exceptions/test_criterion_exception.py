import pytest
from bookland.domain.exceptions import CriterionNotFoundException

def test_criterion_not_found_exception_is_raised():
    with pytest.raises(CriterionNotFoundException) as exc_info:
        raise CriterionNotFoundException()

    assert str(exc_info.value) == "Critério de avaliação não foi encontrado."
