from uuid import uuid4

from bookland.domain.value_objects import Title, Slug
from bookland.domain.entities import Series


def create_series(**overrides):
    base = {
        "id": str(uuid4()),
        "name": Title("Trono de Vidro"),
        "slug": Slug("trono-de-vidro"),
        "description": "Série sobre uma assassina que participa de um torneio para se tornar a campeã do rei.",
    }
    base.update(overrides)

    return Series(**base)
