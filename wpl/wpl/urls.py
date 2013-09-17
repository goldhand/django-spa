from django.conf.urls import patterns, include, url
from rest_framework import routers
from quickstart import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/todo/', include("backbone.urls")),
                       url(r'^api/blog/', include('blog.urls')),
                       url(r'^api/books/', include('books.urls', namespace='books')),
                       url(r'^api', include('snippets.urls')),
                       url(r'^$', 'blog.views.angular_view'),
                       #url(r'^', include(router.urls)),
)
