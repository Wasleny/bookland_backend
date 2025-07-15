from bookland.domain.entities import Series
from bookland.domain.repositories import SeriesRepository


class InMemorySeriesRepository(SeriesRepository):
    def __init__(self) -> None:
        self._series: dict[str, Series] = {}

    async def get_all(self) -> list[Series]:
        return [series for series in self._series.values() if not series.is_deleted]

    async def get_by_id(self, series_id: str) -> Series | None:
        for series in self._series.values():
            if not series.is_deleted and series.id == series_id:
                return series

        return None

    async def create(self, series: Series) -> Series:
        self._series[series.id] = series

        return series

    async def update(self, series: Series) -> Series | None:
        if series.id in self._series:
            self._series[series.id] = series
            return series

        return None

    async def soft_delete(self, series_id: str) -> Series | None:
        series = self._series.get(series_id)

        if series:
            series.soft_delete()
            return series

        return None
