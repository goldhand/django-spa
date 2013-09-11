## Setup

### Requirements

	Django==1.5.2
	argparse==1.2.1
	distribute==0.6.24
	django-debug-toolbar==0.9.4
	django-extensions==1.2.0
	djangorestframework==2.3.7
	ipython==1.0.0
	six==1.3.0
	wsgiref==0.1.2

Assuming you have pip and virtualenv-wrapper:

	pip install -r requirements.pip

### Django Setup

Set up a new django project:

	django-admin.py startproject djangobackbone

Edit your settings.py file in `djangobackbone/djangobackbone/settings.py:

	import os

	DEBUG = True
	TEMPLATE_DEBUG = DEBUG
	ADMINS = () 
	MANAGERS = ADMINS
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.sqlite3', 
		'NAME': 'dev.db',
		'USER': '',
		'PASSWORD': '',
		'PORT': '',
		'HOST': '',
	    }
	}

	ALLOWED_HOSTS = []
	TIME_ZONE = 'America/Phoenix'
	LANGUAGE_CODE = 'en-us'
	SITE_ID = 1
	USE_I18N = True
	USE_L10N = True
	USE_TZ = True
	PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
	PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]
	STATIC_URL = '/static/'
	STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))
	MEDIA_URL = STATIC_URL + 'media/'
	MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))
	TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)
	STATICFILES_DIRS = ()
	STATICFILES_FINDERS = (
	    'django.contrib.staticfiles.finders.FileSystemFinder',
	    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	)
	SECRET_KEY = 'somerandomlygeneratedsequence'
	TEMPLATE_LOADERS = (
	    'django.template.loaders.filesystem.Loader',
	    'django.template.loaders.app_directories.Loader',
	)
	MIDDLEWARE_CLASSES = (
	    'django.middleware.common.CommonMiddleware',
	    'django.contrib.sessions.middleware.SessionMiddleware',
	    'django.middleware.csrf.CsrfViewMiddleware',
	    'django.contrib.auth.middleware.AuthenticationMiddleware',
	    'django.contrib.messages.middleware.MessageMiddleware',
	    'debug_toolbar.middleware.DebugToolbarMiddleware',
	)
	ALLOWED_HOSTS += ['127.0.0.1', '127.0.0.1:8000']
	INTERNAL_IPS = ("127.0.0.1",)
	ROOT_URLCONF = 'wpl.urls'
	WSGI_APPLICATION = 'wpl.wsgi.application'
	INSTALLED_APPS = (
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.sites',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'django_extensions',
	    'debug_toolbar',
	    'rest_framework',
	    'books',
	)
	REST_FRAMEWORK = {
	    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
	}
	LOGGING = {
	    'version': 1,
	    'disable_existing_loggers': False,
	    'filters': {
		'require_debug_false': {
		    '()': 'django.utils.log.RequireDebugFalse'
		}
	    },
	    'handlers': {
		'mail_admins': {
		    'level': 'ERROR',
		    'filters': ['require_debug_false'],
		    'class': 'django.utils.log.AdminEmailHandler'
		}
	    },
	    'loggers': {
		'django.request': {
		    'handlers': ['mail_admins'],
		    'level': 'ERROR',
		    'propagate': True,
		},
	    }
	}


## Create the books django application

Go to your project root directory (where manage.py is) and create a new app called "books" `python manage.py create_app books`

### Backend

Edit the `books/models.py` file:

	from django.db import models


	class Book(models.Model):
	    coverImage = models.ImageField(upload_to='books/cover_images/', blank=True)
	    title = models.CharField(max_length=255, blank=True)
	    author = models.CharField(max_length=255, blank=True)
	    releaseDate = models.DateTimeField(null=True)
	    keywords = models.CharField(max_length=255, blank=True)

	    class Meta:
		ordering = ('releaseDate',)


Create `books/serializers.py`:

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


	class UserSerializer(serializers.ModelSerializer):
		snippets = serializers.PrimaryKeyRelatedField(many=True)

		class Meta:
			model = User
			fields = ('id', 'username', 'snippets')


Edit the `books/views.py` file:

	from django.shortcuts import render
	from django.contrib.auth.models import User

	from rest_framework.response import Response
	from rest_framework.reverse import reverse
	from rest_framework.decorators import api_view
	from rest_framework import generics, viewsets, mixins

	from .models import Book
	from .serializers import BookSerializer, UserSerializer


	@api_view(('GET',))
	def library(request, format=None):
	    return Response({
		'users': reverse('user-list', request=request, format=format),
		'books': reverse('book-list', request=request, format=format)
	    })


	def backbone_view(request):
	    return render(request, 'books/books.html')


	class BookViewSet(viewsets.ModelViewSet):
	    queryset = Book.objects.all()
	    serializer_class = BookSerializer


	class UserViewSet(viewsets.ReadOnlyModelViewSet):
	    queryset = User.objects.all()
	    serializer_class = UserSerializer


Edit the `books/urls.py` file:

	try:
	    from django.conf.urls import *
	except ImportError:  # django < 1.4
	    from django.conf.urls.defaults import *


	from .views import BookViewSet


	book_list = BookViewSet.as_view({
	    'get': 'list',
	    'post': 'create'
	})
	book_detail = BookViewSet.as_view({
	    'get': 'retrieve',
	    'put': 'update',
	    'patch': 'partial_update',
	    'delete': 'destroy'
	})

	urlpatterns = patterns('books.views',
			       url(r'^$', book_list, name='book-list'),
			       url(r'^(?P<pk>[0-9]+)/$', book_detail, name='book-detail'),
			       url(r'^backbone/', 'backbone_view', name='backbone'),
			       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
	)


### Frontend

Within the `books/` directory add a bunch of directories so it looks like this:

	books/
	      models.py
	      views.py
	      urls.py
	      serializers.py
	      static/
	             books/
	                   css/
	                   img/
	                   js/
	                      collections/
	                      lib/
	                      models/
	                      views/
	      templates/
	                books/
	                      includes/
	                      script_templates/


The static files will be added during the backbone part of this guide but first we will build the templates:

In `books/templates/books/` create `base.html`:

	{% load staticfiles %}
	<!doctype html>
	<html lang="en">
	<head>
	  <meta charset="utf-8">
	    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	  <title>{% block meta_title %}{% endblock meta_title %}</title>
	  <meta name="description" content="{% block meta_description %}{% endblock meta_description %}">
	{% block extra_meta %}{% endblock extra_meta %}
	  <link rel="stylesheet" href="{% static 'books/css/jquery-ui-1.10.3.custom.min.css' %}">
	{% block extra_css %}{% endblock extra_css %}
	</head>
	<body>
	{% block main %}{% endblock main %}
	{% csrf_token %}
	<script src="{% static 'books/js/lib/jquery-1.10.2.min.js' %}"></script>
	<script src="{% static 'books/js/lib/jquery-ui-1.10.3.custom.min.js' %}"></script>
	<script src="{% static 'books/js/lib/underscore-min.js' %}"></script>
	<script src="{% static 'books/js/lib/backbone-min.js' %}"></script>
	<script src="{% static 'books/js/lib/backbone.localStorage.js' %}"></script>
	{% block extra_templates %}{% endblock extra_templates %}
	{% block extra_js %}{% endblock extra_js %}
	</body>
	</html>


In `books/templates/books/` create `books.html`:

	{% extends 'books/base.html' %}
	{% load staticfiles %}

	{% block main %}
		{% include 'books/includes/add_book.html' %}
	{% endblock main %}

	{% block extra_js %}
		<script src="{% static 'books/js/models/book.js' %}"></script>
		<script src="{% static 'books/js/collections/library.js' %}"></script>
		<script src="{% static 'books/js/views/book.js' %}"></script>
		<script src="{% static 'books/js/views/library.js' %}"></script>
		<script src="{% static 'books/js/app.js' %}"></script>
	{% endblock extra_js %}

	{% block extra_templates %}
		{% include 'books/script_templates/bookTemplate.html' %}
	{% endblock extra_templates %}

	{% block extra_css %}
		<style>
		body { background-color: #eee; }
		.bookContainer { outline: 1px solid #aaa; width: 350px; height: 130px; background-color: #fff; float: left; margin: 5px; }
		.bookContainer img { float: left; margin: 10px; }
		.bookContainer ul { list-style-type: none; margin-bottom: 0; }
		.bookContainer button { float: right; margin: 10px; }
		#addBook label { width: 100px; margin-right: 10px; text-align: right; line-height: 25px; }
		#addBook label, #addBook input { display: block; margin-bottom: 10px; float: left; }
		#addBook label[for="title"], #addBook label[for="releaseDate"] { clear: both; }
		#addBook button { display: block; margin: 5px 20px 10px 10px; float: right; clear: both; }
		#addBook div { width: 560px; }
		#addBook div:after { content: ""; display: block; height: 0; visibility: hidden; clear: both; font-size: 0; line-height: 0; }
		</style>
	{% endblock extra_css %}


In `books/templates/books/includes/` create `add_book.html`:

	{# This should be a django form but im lazy so I copied from the backbone tutorial #}
	<div id="books">
	    <form id="addBook" action="#" enctype="multipart/form-data">
		<div>
		    <label for="coverImage">CoverImage: </label><input id="coverImage" type="file" />
		    <label for="title">Title: </label><input id="title" type="text" />
		    <label for="author">Author: </label><input id="author" type="text" />
		    <label for="releaseDate">Release date: </label><input id="releaseDate" type="text" />
		    <label for="keywords">Keywords: </label><input id="keywords" type="text" />
		    <button id="add">Add</button>
		</div>
	    </form>
	</div>


In `books/templates/books/script_templates/` create `bookTemplate.html`:

	{% load static %}
	<script id="bookTemplate" type="text/template">
	    <img src="{{ MEDIA_URL }}/<%= coverImage %>"/>
	    <ul>
		<li><%= title %></li>
		<li><%= author %></li>
		<li><%= releaseDate %></li>
		<li><%= keywords %></li>
	    </ul>

	    <button class="delete">Delete</button>
	</script>



Ok thats it for the Django parts, we should have a fully functioning restful api for our library

Your books app should look like this now:

	books/
	      models.py
	      views.py
	      urls.py
	      serializers.py
	      static/
	             books/
	                   css/
	                   img/
	                   js/
	                      collections/
	                      lib/
	                      models/
	                      views/
	      templates/
	                books/
			      base.html
			      books.html
	                      includes/
				       add_book.html
	                      script_templates/
					       bookTemplate.html


## Backbone


