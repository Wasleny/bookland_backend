from uuid import uuid4
from bookland.domain.value_objects.name_vo import Name
from bookland.domain.entities.series import Series


def create_series(**overrides):
    base = {"id": str(uuid4()), "name": Name("Trono de Vidro")}
    base.update(overrides)

    return Series(**base)
