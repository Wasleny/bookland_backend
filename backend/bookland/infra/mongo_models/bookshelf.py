from bookland.domain.value_objects.label_vo import Label
from bookland.domain.value_objects.slug_vo import Slug
from bookland.domain.exceptions.bookshelf_exception import InvalidBookshelfException


class Bookshelf:
    def __init__(self, id: str, name: Label, slug: Slug):
        self._validate_bookshelf(name, slug)

        self._id = id
        self._name = name
        self._slug = slug

    @staticmethod
    def _validate_bookshelf(name, slug):
        Bookshelf._validate_name(name)
        Bookshelf._validate_slug(slug)

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, Label):
            raise InvalidBookshelfException("Nome deve ser uma instância de Label")

    @staticmethod
    def _validate_slug(slug):
        if not isinstance(slug, Slug):
            raise InvalidBookshelfException("Slug deve ser uma instância de Slug")

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def slug(self):
        return self._slug
