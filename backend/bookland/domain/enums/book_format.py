from enum import Enum


class BookFormat(str, Enum):
    HARDCOVER = "hardcover"
    PAPERBACK = "paperback"
    AUDIOBOOK = "audiobook"
    EBOOK = "ebook"
    LARGE_PRINT = "large print"
