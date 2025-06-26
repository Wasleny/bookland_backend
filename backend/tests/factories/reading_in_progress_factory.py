from uuid import uuid4
from bookland.domain.entities.reading_in_progress import ReadingInProgress


def create_reading_in_progress(**overrides) -> ReadingInProgress:
    base = {
        "id": str(uuid4()),
        "book_id": str(uuid4()),
        "user_id": str(uuid4()),
        "progress": 50,
    }
    base.update(overrides)

    return ReadingInProgress(**base)
