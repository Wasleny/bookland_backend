SERIES_NOT_FOUND = "Série não foi encontrada."


class InvalidSeriesException(Exception): ...


class SeriesNotFoundException(Exception):
    def __init__(self, message=SERIES_NOT_FOUND):
        super().__init__(message)
