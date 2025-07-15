from bookland.domain.entities import Review
from bookland.infra.mongo_models import ReviewDocument, ReadingCriteriaModel
from bookland.domain.value_objects import Rating, Date, ReadingCriteria, Label


class ReviewMapper:
    @staticmethod
    def to_domain(document: ReviewDocument) -> Review:
        return Review(
            id=document.id,
            user_id=document.user_id,
            book_id=document.book_id,
            rating=Rating(document.rating),
            body=document.body,
            spoiler=document.spoiler,
            start_date=Date(document.start_date),
            end_date=Date(document.end_date),
            most_recent_reading=document.most_recent_reading,
            rating_composition_criteria=[
                ReadingCriteria(
                    Label(reading_criteria.criterion), Rating(reading_criteria.rating)
                )
                for reading_criteria in document.rating_composition_criteria
            ],
            independent_rating_criteria=[
                ReadingCriteria(
                    Label(reading_criteria.criterion), Rating(reading_criteria.rating)
                )
                for reading_criteria in document.independent_rating_criteria
            ],
        )

    @staticmethod
    def to_document(review: Review) -> ReviewDocument:
        return ReviewDocument(
            id=review.id,
            user_id=review.user_id,
            book_id=review.book_id,
            rating=review.rating,
            body=review.body,
            spoiler=review.spoiler,
            start_date=review.start_date,
            end_date=review.end_date,
            most_recent_reading=review.most_recent_reading,
            rating_composition_criteria=[
                ReadingCriteriaModel(
                    criterion=reading_criteria.criterion.value,
                    rating=reading_criteria.rating.value,
                )
                for reading_criteria in review.rating_composition_criteria
            ],
            independent_rating_criteria=[
                ReadingCriteriaModel(
                    criterion=reading_criteria.criterion.value,
                    rating=reading_criteria.rating.value,
                )
                for reading_criteria in review.independent_rating_criteria
            ],
        )
