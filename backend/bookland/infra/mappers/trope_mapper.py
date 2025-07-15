from bookland.domain.entities import Trope
from bookland.domain.value_objects import Label, Slug
from bookland.infra.mongo_models import TropeDocument


class TropeMapper:
    @staticmethod
    def to_domain(document: TropeDocument) -> Trope:
        return Trope(
            id=document.id,
            name=Label(document.name),
            name_pt_br=Label(document.name_pt_br),
            slug=Slug(document.slug),
        )

    @staticmethod
    def to_document(trope: Trope) -> TropeDocument:
        return TropeDocument(
            id=trope.id,
            name=trope.name.value,
            name_pt_br=trope.name_pt_br.value,
            slug=trope.slug.value,
        )
