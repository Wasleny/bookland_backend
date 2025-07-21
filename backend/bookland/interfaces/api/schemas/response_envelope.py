from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")


class ResponseEnvelopeSchema(BaseModel, Generic[T]):
    message: str
    data: T | list[T]

    @classmethod
    def from_entity(cls, data, message):
        return cls(
            message=message,
            data=data,
        )

