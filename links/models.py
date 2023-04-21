from django.db import models


class ShortLink(models.Model):
    slug = models.CharField(max_length=100, unique=True, blank=False, null=False)
    target = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return self.slug
