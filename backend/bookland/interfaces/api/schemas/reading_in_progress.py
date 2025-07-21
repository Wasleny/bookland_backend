from pydantic import BaseModel, Field


class ReadingInProgressSchema(BaseModel):
    book_id: str = Field(..., description="ID do livro")
    progress: int = Field(
        ..., ge=0, lt=100, description="Porcentagem de progresso da leitura"
    )


class CreateReadingInProgressSchema(ReadingInProgressSchema): ...


class UpdateReadingInProgressSchema(ReadingInProgressSchema): ...


class ReadingInProgressResponseSchema(BaseModel):
    id: str = Field(..., description="ID da leitura em progresso")
    book: dict = Field(..., description="Livro associado à leitura em progresso")
    user_id: str = Field(..., description="ID do usuário que está lendo")
    progress: str = Field(..., description="Progresso da leitura em porcentagem")

    @classmethod
    def from_entity(cls, reading):
        return cls(
            id=reading.id,
            book={
                "id": reading.book.id,
                "title": reading.book.title,
                "cover": reading.book.cover,
            },
            user_id=reading.user_id,
            progress=reading.progress,
        )
