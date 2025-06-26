from bookland.domain.repositories.author_repository import AuthorRepository


class SoftDeleteAuthorUseCase:
    def __init__(self, repository: AuthorRepository):
        self._repository = repository

    def execute(self, author_id: str) -> None:
        self._repository.soft_delete(author_id)
