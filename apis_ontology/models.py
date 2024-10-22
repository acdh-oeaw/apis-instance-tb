from apis_core.apis_entities.models import AbstractEntity

class BaseEntity(AbstractEntity):
    """
    Base class for all entities.
    """

    class Meta:
        abstract = True
