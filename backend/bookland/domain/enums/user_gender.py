from enum import Enum


class UserGender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non-binary"
    UNSPECIFIED = "unspecified"
