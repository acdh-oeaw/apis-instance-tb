from apis_core.apis_entities.abc import E74_Group, E21_Person, E53_Place
from apis_core.apis_entities.models import AbstractEntity
from apis_core.history.models import VersionMixin

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseEntity(AbstractEntity):
    """
    Base class for all entities.
    """

    class Meta:
        abstract = True


class TitlesMixin(models.Model):
    """
    Mixin for fields shared between work-like entities.
    """

    title = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name=_("Titel"),
    )

    subtitle = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name=_("Untertitel"),
    )

    class Meta:
        abstract = True


class Work(VersionMixin, TitlesMixin, BaseEntity):
    """
    The abstract notion of an intellectual creation, irrespective
    of its exact transmitted version, language or other form.
    """

    class Meta:
        verbose_name = _("werk")
        verbose_name_plural = _("werke")


class Expression(VersionMixin, TitlesMixin, BaseEntity):
    """
    A concrete representation of a given Work,
    captured in signs, images, audio signals,...
    """

    class Meta:
        verbose_name = _("werksexpression")
        verbose_name_plural = _("werksexpressionen")


class Person(VersionMixin, BaseEntity, E21_Person):

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Personen")


class Place(VersionMixin, BaseEntity, E53_Place):

    class Meta:
        verbose_name = _("Ort")
        verbose_name_plural = _("Orte")


class Group(VersionMixin, BaseEntity, E74_Group):

    class Meta:
        verbose_name = _("Körperschaft")
        verbose_name_plural = _("Körperschaften")
