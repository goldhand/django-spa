from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Post, LANGUAGE_CHOICES


class PostSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.Field(source='owner.username')

	class Meta:
		model = Post
		fields = ('url', 'owner', 'title', 'language', 'content')

