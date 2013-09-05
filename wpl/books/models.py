from django.db import models


class Book(models.Model):
    coverImage = models.ImageField(upload_to='books/cover_images/', blank=True)
    title = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255, blank=True)
    releaseDate = models.DateTimeField(blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ('releaseDate',)
