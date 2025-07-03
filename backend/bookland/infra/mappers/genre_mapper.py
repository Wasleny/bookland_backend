from bookland.domain.entities import Genre
from bookland.domain.value_objects import Label, Slug
from bookland.infra.mongo_models import GenreDocument


class GenreMapper:
    @staticmethod
    def to_domain(document: GenreDocument) -> Genre:
        return Genre(
            id=document.id,
            name=Label(document.name),
            slug=Slug(document.slug),
        )

    @staticmethod
    def to_document(genre: Genre) -> GenreDocument:
        return GenreDocument(
            id=genre.id,
            name=genre.name.value,
            slug=genre.slug.value,
        )
