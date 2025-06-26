from uuid import uuid4
from datetime import date
from bookland.domain.value_objects.date_vo import Date
from bookland.domain.value_objects.reading_criteria_vo import ReadingCriteria
from bookland.domain.entities.review import Review


def create_review(**overrides):
    base = {
        "id": str(uuid4()),
        "user_id": str(uuid4()),
        "book_id": str(uuid4()),
        "rating": 5,
        "body": "Esse livro transformou a minha vida",
        "spoiler": False,
        "start_date": Date(date(2025, 6, 20)),
        "end_date": Date(date(2025, 6, 20)),
        "most_recent_reading": False,
        "rating_composition_criteria": [
            ReadingCriteria("Enredo", 5),
            ReadingCriteria("Escrita", 5),
        ],
        "independent_rating_criteria": [ReadingCriteria("Impacto Emocional", 5)],
    }
    base.update(overrides)

    return Review(**base)
