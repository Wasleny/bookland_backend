from uuid import uuid4

from bookland.domain.entities import UserBook


def create_user_book(**overrides):
    base = {
        "id": str(uuid4()),
        "book_id": str(uuid4()),
        "user_id": str(uuid4()),
        "default_bookshelf_id": str(uuid4()),
    }
    base.update(overrides)

    return UserBook(**base)
