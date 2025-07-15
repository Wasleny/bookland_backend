from uuid import uuid4
from datetime import date

from bookland.domain.value_objects import Date, ReadingCriteria, Label, Rating
from bookland.domain.entities import Review


def create_review(**overrides):
    base = {
        "id": str(uuid4()),
        "user_id": str(uuid4()),
        "book_id": str(uuid4()),
        "rating": Rating(5),
        "body": "Esse livro transformou a minha vida",
        "spoiler": False,
        "start_date": Date(date(2025, 6, 20)),
        "end_date": Date(date(2025, 6, 20)),
        "most_recent_reading": False,
        "rating_composition_criteria": [
            ReadingCriteria(Label("Enredo"), Rating(5)),
            ReadingCriteria(Label("Escrita"), Rating(5)),
        ],
        "independent_rating_criteria": [
            ReadingCriteria(Label("Impacto Emocional"), Rating(5))
        ],
    }
    base.update(overrides)

    return Review(**base)
