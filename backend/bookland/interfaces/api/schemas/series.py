from pydantic import BaseModel, Field


class SeriesSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=30, description="Nome da série")
    slug: str = Field(..., min_length=2, max_length=30, description="Slug da série")
    description: str = Field(
        ..., min_length=2, max_length=200, description="Descrição da série"
    )


class CreateSeriesSchema(SeriesSchema): ...


class UpdateSeriesSchema(SeriesSchema): ...


class SeriesResponseSchema(BaseModel):
    id: str = Field(..., description="ID do autor")
    name: str = Field(..., description="Nome da série")
    slug: str = Field(..., description="Slug da série")
    description: str = Field(..., description="Descrição da série")

    @classmethod
    def from_entity(cls, series):
        return cls(
            id=series.id,
            name=series.name.value,
            slug=series.slug.value,
            description=series.description,
        )
