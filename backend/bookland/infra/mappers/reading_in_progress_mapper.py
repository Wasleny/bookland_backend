from bookland.domain.entities import ReadingInProgress
from bookland.infra.mongo_models import ReadingInProgressDocument


class ReadingInProgressMapper:
    @staticmethod
    def to_domain(document: ReadingInProgressDocument) -> ReadingInProgress:
        return ReadingInProgress(
            id=document.id,
            book_id=document.book_id,
            user_id=document.user_id,
            progress=document.progress,
        )

    @staticmethod
    def to_document(reading: ReadingInProgress) -> ReadingInProgressDocument:
        return ReadingInProgressDocument(
            id=reading.id,
            book_id=reading.book_id,
            user_id=reading.user_id,
            progress=reading.progress,
        )
