from bookland.domain.entities import Series
from bookland.domain.value_objects import Title, Slug
from bookland.infra.mongo_models import SeriesDocument


class SeriesMapper:
    @staticmethod
    def to_domain(document: SeriesDocument) -> Series:
        return Series(
            id=document.id,
            name=Title(document.name),
            slug=Slug(document.slug),
            description=document.description,
        )

    @staticmethod
    def to_document(series: Series) -> SeriesDocument:
        return SeriesDocument(
            id=series.id,
            name=series.name.value,
            slug=series.slug.value,
            description=series.description,
        )
