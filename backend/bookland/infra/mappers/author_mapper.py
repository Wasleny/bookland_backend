from bookland.domain.entities import Author
from bookland.domain.value_objects import Name
from bookland.infra.mongo_models import AuthorDocument


class AuthorMapper:
    @staticmethod
    def to_domain(document: AuthorDocument) -> Author:
        return Author(
            id=document.id, name=Name(document.name), nationality=document.nationality
        )

    @staticmethod
    def to_document(author: Author) -> AuthorDocument:
        return AuthorDocument(
            id=author.id, name=author.name.value, nationality=author.nationality
        )
