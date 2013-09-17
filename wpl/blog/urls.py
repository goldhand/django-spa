from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

import views
from .views import PostViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

# The API URLs are now determined automatically by the router.
# Additionally. we include the login URLs for the browseable API.
post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns('blog.views',
                       url(r'^$', 'blog'),
                       url(r'^posts/$', post_list, name='post-list'),
                       url(r'^posts/(?P<pk>[0-9]+)/$', post_detail, name='post-detail'),
                       url(r'^angular/partials/post-list/', 'angular_view_post_list'),
                       url(r'^angular/partials/post-detail/', 'angular_view_post_detail'),
)

