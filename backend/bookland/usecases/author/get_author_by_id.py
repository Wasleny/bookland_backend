from bookland.domain.entities.author import Author
from bookland.domain.repositories.author_repository import AuthorRepository


class GetAuthorByIdUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    def execute(self, author_id: str) -> Author | None:
        return self._repository.get_by_id(author_id)
