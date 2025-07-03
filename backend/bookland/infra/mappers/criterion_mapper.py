from bookland.domain.entities import Criterion
from bookland.domain.value_objects import Label
from bookland.infra.mongo_models import CriterionDocument


class CriterionMapper:
    @staticmethod
    def to_domain(document: CriterionDocument) -> Criterion:
        return Criterion(
            id=document.id,
            name=Label(document.name),
            description=document.description,
            user_id=document.user_id,
        )

    @staticmethod
    def to_document(criterion: Criterion) -> CriterionDocument:
        return CriterionDocument(
            id=criterion.id,
            name=criterion.name.value,
            description=criterion.description,
            user_id=criterion.user_id,
        )
