from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES 


class SnippetSerializer(serializers.Serializer):
	pk = serializers.Field()
	title = serializers.CharField(max_length=100, required=False)
	code = serializers.CharField(max_length=100000, widget=widgets.Textarea)
	linenos = serializers.BooleanField(required=False)
	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

	def restore_object(self, attrs, instance=None):
		if instance:
			instance.title = attrs.get('title', instance.title)
			instance.code = attrs.get('code', instance.code)
			instance.linenos = attrs.get('linenos', instance.linenos)
			instance.language = attrs.get('language', instance.language)
			instance.style = attrs.get('style', instance.style)
			return instance

		return Snippet(**attrs)


class SnippetSerializer(serializers.ModelSerializer):
	owner = serializers.Field(source='owner.username')
	class Meta:
		model = Snippet
		fields = ('id', 'title', 'code', 'linenos', 
			  'language', 'style', 'owner')
		

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.Field(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

	class Meta:
		model = Snippet
		fields = ('url', 'highlight', 'owner',
			  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.ModelSerializer):
	snippets = serializers.PrimaryKeyRelatedField(many=True)

	class Meta:
		model = User
		fields = ('id', 'username', 'snippets')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail')

	class Meta:
		model = User
		fields = ('url', 'username', 'snippets')




