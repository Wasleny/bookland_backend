EMAIL_ALREADY_EXISTS = "E-mail já cadastrado no sistema."
USER_NOT_FOUND = "Usuário não encontrado."


class InvalidUserException(Exception): ...


class UserNotFoundException(Exception):
    def __init__(self, message=USER_NOT_FOUND):
        super().__init__(message)


class EmailAlreadyExistsException(Exception):
    def __init__(self, message=EMAIL_ALREADY_EXISTS):
        super().__init__(message)
