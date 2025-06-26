from bookland.domain.entities.author import Author
from bookland.domain.repositories.author_repository import AuthorRepository


class InMemoryAuthorRepository(AuthorRepository):
    def __init__(self):
        self._authors: dict[str, Author] = {}

    def get_all(self) -> list[Author]:
        return [author for author in self._authors.values() if not author.is_deleted]

    def get_by_id(self, author_id: str) -> Author | None:
        for author in self._authors.values():
            if not author.is_deleted and author.id == author_id:
                return author

        return None

    def create(self, author: Author) -> None:
        self._authors[author.id] = author

    def update(self, author: Author) -> None:
        if author.id in self._authors:
            self._authors[author.id] = author

    def soft_delete(self, author_id: str) -> None:
        author = self._authors.get(author_id)

        if author:
            author.soft_delete()
