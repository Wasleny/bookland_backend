from abc import ABC, abstractmethod
from bookland.domain.entities.series import Series


class SeriesRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Series]: ...

    @abstractmethod
    async def get_by_id(self, series_id: str) -> Series: ...

    @abstractmethod
    async def create(self, series: Series) -> Series: ...

    @abstractmethod
    async def update(self, series: Series) -> Series | None: ...

    @abstractmethod
    async def soft_delete(self, series_id: str) -> None: ...
