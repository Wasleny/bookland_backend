from pydantic import BaseModel, Field


class AuthorSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=30, description="Nome do autor")
    nationality: str | None = Field(
        ..., min_length=3, max_length=20, description="Nome do país de origem do autor"
    )


class CreateAuthorSchema(AuthorSchema): ...


class UpdateAuthorSchema(AuthorSchema): ...


class AuthorResponseSchema(BaseModel):
    id: str = Field(..., description="ID do autor")
    name: str = Field(..., description="Nome do autor")
    nationality: str = Field(..., description="País de origem do autor")

    @classmethod
    def from_entity(cls, author):
        return cls(id=author.id, name=author.name.value, nationality=author.nationality)
