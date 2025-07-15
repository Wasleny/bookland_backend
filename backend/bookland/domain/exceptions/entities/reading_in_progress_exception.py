READING_IN_PROGRESS_NOT_FOUND = "Leitura em andamento não foi encontrada."


class InvalidReadingInProgressException(Exception): ...


class ReadingInProgressNotFoundException(Exception):
    def __init__(self, message=READING_IN_PROGRESS_NOT_FOUND):
        super().__init__(message)
