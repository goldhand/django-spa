from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.decorators import api_view

from rest_framework import generics, permissions, viewsets

from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(('GET',))
def blog(request, format=None):
    return Response({
        'posts': reverse('post-list', request=request, format=format)
    })


class PostList(generics.ListCreateAPIView):
    """
	Class based view using generic views
	List all snippets, or create a new snippet.
	"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.owner = self.request.user


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
	Class based view using generic views
	Retrieve, update or delete a code snippet.
	"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def pre_save(self, obj):
        obj.owner = self.request.user


class PostViewSet(viewsets.ModelViewSet):
    """
	This viewset automatically provides 'list', 'create', 'retrieve',
	'update', and 'destroy' actions.
	Additionally we also provide an extra 'highlight' action.
	"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user




