from django.db import models


class Book(models.Model):
    coverImage = models.URLField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255, blank=True)
    releaseDate = models.DateField(auto_now_add=True)
    keywords = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ('releaseDate',)
