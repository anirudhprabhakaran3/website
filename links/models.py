from django.db import models
# Create your models here.


class ShortLink(models.Model):
    slug = models.CharField(max_length=200, blank=False, null=False)
    target = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.slug
