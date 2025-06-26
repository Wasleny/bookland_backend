from bookland.domain.value_objects.label_vo import Label
from bookland.domain.value_objects.slug_vo import Slug
from bookland.domain.exceptions.genre_exception import InvalidGenreException
from datetime import datetime


class Genre:
    def __init__(self, id: str, name: Label, slug: Slug):
        self._validate_genre(name, slug)

        self._id = id
        self._name = name
        self._slug = slug
        self._deleted_at = None

    @staticmethod
    def _validate_genre(name, slug):
        Genre._validate_name(name)
        Genre._validate_slug(slug)

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, Label):
            raise InvalidGenreException("Nome deve ser uma instância de Label")

    @staticmethod
    def _validate_slug(slug):
        if not isinstance(slug, Slug):
            raise InvalidGenreException("Slug deve ser uma instância de Slug")

    def soft_delete(self):
        if not self.is_deleted:
            self._deleted_at = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def slug(self):
        return self._slug

    @property
    def is_deleted(self):
        return self._deleted_at is not None

    @property
    def deleted_at(self):
        return self._deleted_at
