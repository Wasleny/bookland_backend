from pydantic import BaseModel, Field


class GenreResponseSchema(BaseModel):
    id: str = Field(..., description="ID do gênero literário")
    name: str = Field(..., description="Nome do gênero literário")
    slug: str = Field(..., description="Slug para o gênero literário")

    @classmethod
    def from_entity(cls, genre):
        return cls(id=genre.id, name=genre.name.value, slug=genre.slug.value)
