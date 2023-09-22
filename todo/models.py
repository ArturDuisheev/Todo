from django.db import models
from pytils.translit import slugify
from django.utils.translation import gettext as _

from reccuring.models import BaseModel


class Task(BaseModel):
    title = models.CharField(
        _('title'),
        max_length=100)
    description = models.TextField(
        _('description')
    )
    completed = models.BooleanField(
        _('completed'),
        default=False
    )
    slug = models.SlugField(
        _('slug'),
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:100]
        super().save(*args, **kwargs)
