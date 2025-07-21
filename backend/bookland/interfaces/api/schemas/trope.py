from pydantic import BaseModel, Field


class TropeResponseSchema(BaseModel):
    id: str = Field(..., description="ID da trope literária")
    name: str = Field(..., description="Nome da trope literária")
    name_pt_br: str = Field(..., description="Nome da trope literária em português")
    slug: str = Field(..., description="Slug para a trope literária")

    @classmethod
    def from_entity(cls, trope):
        return cls(
            id=trope.id,
            name=trope.name.value,
            name_pt_br=trope.name_pt_br.value,
            slug=trope.slug.value,
        )
