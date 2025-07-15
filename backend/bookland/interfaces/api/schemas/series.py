from pydantic import BaseModel, Field


class SeriesSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=30, description="Nome da série")


class CreateSeriesSchema(SeriesSchema): ...


class UpdateSeriesSchema(SeriesSchema): ...


class SeriesResponseSchema(BaseModel):
    id: str = Field(..., description="ID do autor")
    name: str = Field(..., description="Nome da série")

    @classmethod
    def from_entity(cls, series):
        return cls(id=series.id, name=series.name.value)
