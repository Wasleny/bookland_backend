from pydantic import BaseModel, Field


class UserBookSchema(BaseModel):
    book_id: str = Field(..., description="ID do livro")
    default_bookshelf_id: str = Field(
        ..., description="ID da estante padrão onde o livro está localizado"
    )


class CreateUserBookSchema(UserBookSchema): ...


class UpdateUserBookSchema(UserBookSchema): ...


class UserBookResponseSchema(BaseModel):
    id: str = Field(..., description="ID da relação entre usuário e livro")
    book: dict = Field(..., description="Detalhes do livro associado")
    user_id: str = Field(..., description="ID do usuário associado")
    default_bookshelf: dict = Field(..., description="Detalhes da estante padrão")

    @classmethod
    def from_entity(cls, user_book):
        return cls(
            id=user_book.id,
            book={
                "id": user_book.book_id,
                "title": user_book.book.title.value,
                "cover": user_book.book.cover,
            },
            user_id=user_book.user_id,
            default_bookshelf={
                "id": user_book.default_bookshelf_id,
                "name": user_book.default_bookshelf.name.value,
                "slug": user_book.default_bookshelf.slug.value,
            },
        )
