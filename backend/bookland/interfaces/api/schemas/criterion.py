from pydantic import BaseModel, Field


class CriterionSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=30, description="Nome do critério")
    description: str = Field(
        ...,
        min_length=10,
        max_length=200,
        description="Descrição do que o critério busca avaliar.",
    )


class CreateCriterionSchema(CriterionSchema): ...


class UpdateCriterionSchema(CriterionSchema): ...


class CriterionResponseSchema(BaseModel):
    id: str = Field(..., description="ID do critério")
    name: str = Field(..., description="Nome do critério")
    description: str = Field(
        ..., description="Descrição do que o critério busca avaliar"
    )
    user_id: str = Field(..., description="ID do usuário criador do critério")

    @classmethod
    def from_entity(cls, criterion):
        return cls(
            id=criterion.id,
            name=criterion.name.value,
            description=criterion.description,
            user_id=criterion.user_id,
        )
