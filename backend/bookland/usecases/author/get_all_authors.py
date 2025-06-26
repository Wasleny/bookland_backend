from bookland.domain.entities.author import Author
from bookland.domain.repositories.author_repository import AuthorRepository


class GetAllAuthorsUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    def execute(self) -> list[Author]:
        return self._repository.get_all()
