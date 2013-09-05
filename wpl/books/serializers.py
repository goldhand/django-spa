from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    coverImage = serializers.ImageField(required=False)
    author = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    releaseDate = serializers.DateField(required=False)
    keywords = serializers.CharField(required=False)

    class Meta:
        model = Book


