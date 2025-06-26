from uuid import uuid4
from bookland.domain.value_objects.label_vo import Label
from bookland.domain.entities.user_book import UserBook


def create_user_book(**overrides):
    base = {
        "id": str(uuid4()),
        "book_id": str(uuid4()),
        "user_id": str(uuid4()),
        "default_bookshelf": Label("Lidos"),
    }
    base.update(overrides)

    return UserBook(**base)
