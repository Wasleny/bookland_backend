from bookland.domain.entities.author import Author
from bookland.domain.repositories.author_repository import AuthorRepository


class InMemoryAuthorRepository(AuthorRepository):
    def __init__(self):
        self._authors: dict[str, Author] = {}

    async def get_all(self) -> list[Author]:
        return [author for author in self._authors.values() if not author.is_deleted]

    async def get_by_id(self, author_id: str) -> Author | None:
        for author in self._authors.values():
            if not author.is_deleted and author.id == author_id:
                return author

        return None

    async def create(self, author: Author) -> Author:
        self._authors[author.id] = author

        return author

    async def update(self, author: Author) -> Author | None:
        if author.id in self._authors:
            self._authors[author.id] = author
            return author

        return None

    async def soft_delete(self, author_id: str) -> None:
        author = self._authors.get(author_id)

        if author:
            author.soft_delete()
