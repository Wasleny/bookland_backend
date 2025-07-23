from bookland.domain.entities import Trope
from bookland.domain.repositories import TropeRepository


class InMemoryTropeRepository(TropeRepository):
    def __init__(self) -> None:
        self._tropes: dict[str, Trope] = {}

    async def get_all(self) -> list[Trope]:
        return [trope for trope in self._tropes.values() if not trope.is_deleted]

    async def get_many_by_id(self, tropes_id):
        raise NotImplementedError("...")
