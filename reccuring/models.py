from django.db import models

from django.utils.translation import gettext as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at'),
        help_text=_('Date time on which the object was created.')
    )

    class Meta:
        abstract = True
