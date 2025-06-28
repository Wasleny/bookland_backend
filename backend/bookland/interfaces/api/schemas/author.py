from pydantic import BaseModel


class AuthorCreateSchema(BaseModel):
    name: str
    nationality: str | None = None


class AuthorResponseSchema(BaseModel):
    id: str
    name: str
    nationality: str | None
