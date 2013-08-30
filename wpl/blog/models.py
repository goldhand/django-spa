from django.db import models

from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	content = models.TextField()
	language = models.CharField(choices=LANGUAGE_CHOICES,
			default='python',
			max_length=100)
	owner = models.ForeignKey('auth.user', related_name='posts')

	class Meta:
		ordering = ('created',)

