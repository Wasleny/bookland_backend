from bookland.domain.entities.author import Author
from bookland.domain.repositories.author_repository import AuthorRepository


class UpdateAuthorUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    def execute(self, author: Author) -> None:
        self._repository.update(author)
