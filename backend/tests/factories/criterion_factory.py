from uuid import uuid4
from bookland.domain.entities.criterion import Criterion
from bookland.domain.value_objects.label_vo import Label


def create_criterion(**overrides) -> Criterion:
    base = {
        "id": str(uuid4()),
        "name": Label("Ritmo"),
        "description": "Avalia o ritmo da história, se é muito lenta, se é muito acelerada ou se tem um ritmo balanceado",
        "user_id": str(uuid4()),
    }
    base.update(overrides)

    return Criterion(**base)
