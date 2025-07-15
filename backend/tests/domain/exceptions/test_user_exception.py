import pytest
from bookland.domain.exceptions import (
    UserNotFoundException,
    EmailAlreadyExistsException,
)


def test_user_not_found_exception_is_raised():
    with pytest.raises(UserNotFoundException) as exc_info:
        raise UserNotFoundException()

    assert str(exc_info.value) == "Usuário não encontrado."


def test_email_already_exists_exception_is_raised():
    with pytest.raises(EmailAlreadyExistsException) as exc_info:
        raise EmailAlreadyExistsException()

    assert str(exc_info.value) == "E-mail já cadastrado no sistema."
