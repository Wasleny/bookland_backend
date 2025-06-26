from uuid import uuid4
import random
import string
from bookland.domain.entities.author import Author
from bookland.domain.value_objects.name_vo import Name


def create_author(**overrides) -> Author:
    random_letter = random.choice(string.ascii_uppercase)

    base = {
        "id": str(uuid4()),
        "name": Name(f"Autor {random_letter}"),
        "nationality": "Brasil",
    }
    base.update(overrides)

    return Author(**base)
