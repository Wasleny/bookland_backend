from abc import ABC, abstractmethod
from bookland.domain.entities.series import Series


class SeriesRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Series]: ...

    @abstractmethod
    def get_by_id(self, series_id: str) -> Series: ...

    @abstractmethod
    def create(self, series: Series) -> None: ...

    @abstractmethod
    def update(self, series: Series) -> None: ...

    @abstractmethod
    def soft_delete(self, series_id: str) -> None: ...
