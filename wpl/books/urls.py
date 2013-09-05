from rest_framework.urlpatterns import format_suffix_patterns

try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter

import views
from .views import BookViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', views.BookViewSet)

# The API URLs are now determined automatically by the router.
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
                       url(r'^backbone/', 'backbone_view', name='backbone')
)
urlpatterns = patterns('books.views',
                       url(r'^$',
                           views.BookList.as_view(),
                           name='book-list'),
                       url(r'^(?P<pk>[0-9]+)/$',
                           views.BookDetail.as_view(),
                           name='book-detail'),
                       url(r'^backbone/', 'backbone_view', name='backbone')
)

urlpatterns = format_suffix_patterns(urlpatterns)
