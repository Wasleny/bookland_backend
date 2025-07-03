from pydantic import BaseModel, Field


class TropeResponseSchema(BaseModel):
    id: str = Field(..., description="ID da trope literária")
    name: str = Field(..., description="Nome da trope literária")
    slug: str = Field(..., description="Slug para a trope literária")

    @classmethod
    def from_entity(cls, trope):
        return cls(id=trope.id, name=trope.name.value, slug=trope.slug.value)
