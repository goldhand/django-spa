from django.http import Http404
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.views import APIView
from rest_framework.decorators import api_view, link

from rest_framework import mixins, generics, status, permissions, renderers, viewsets


from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(('GET',))
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'snippets': reverse('snippet-list', request=request, format=format),
		'blog': reverse('blog.views.blog', request=request, format=format)
	})


class SnippetHighlight(generics.GenericAPIView):
	queryset = Snippet.objects.all()
	renderer_classes = (renderers.StaticHTMLRenderer,)

	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)




@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
	"""
	Function View
	List all snippets, or create a new snippet.
	"""
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return Response(serializer.data)
	
	elif request.method == 'POST':
		serializer = SnippetSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetList(APIView):
	"""
	Class based view
	List all snippets, or create a new snippet.
	"""
	def get(self, request, format=None):
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return Response(serializer.data)
		
	def post(self, request, format=None):
		serializer = SnippetSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
	"""
	Class based view using mixins
	List all snippets, or create a new snippet.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
		

class SnippetList(generics.ListCreateAPIView):
	"""
	Class based view using generic views
	List all snippets, or create a new snippet.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			IsOwnerOrReadOnly)

	def pre_save(self, obj):
		obj.owner = self.request.user


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
	"""
	Function View
	Retrieve, update or delete a code snippet.
	"""
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SnippetSerializer(snippet, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class SnippetDetail(APIView):
	"""
	Class based view
	Retrieve, update or delete a code snippet.
	"""
	def get_object(self, pk):
		try:
			return Snippet.objects.get(pk=pk)
		except Snippet.DoesNotExist:
			raise Http404
	def get(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = SnippetSerializer(snippet)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = SnippetSerializer(snippet, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		snippet = self.get_object(pk)
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	

class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
	"""
	Class based view using mixins
	Retrieve, update or delete a code snippet.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Class based view using generic views
	Retrieve, update or delete a code snippet.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def pre_save(self, obj):
		obj.owner = self.request.user


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			IsOwnerOrReadOnly)
	

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides 'list' and 'detail' actions.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides 'list', 'create', 'retrieve',
	'update', and 'destroy' actions.
	Additionally we also provide an extra 'highlight' action.

	#Python
	import urllib, json
	json_str = urllib.URLopener().open('http://127.0.0.1:8000/snippets/')
	python_json_object = json.load(json_str)

	#JavaScript
	var json_str = $.getJSON('/snippets/.json', function(data) {return data;});
	var json_obj = $.parseJSON(json_str['responseText']);
	var json_obj_results = json_obj['results'];
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	@link(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)
	
	def pre_save(self, obj):
		obj.owner = self.request.user




'''
old:
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser

class JSONResponse(HttpResponse):
	
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


data = JSONParser().parse(request)
serializer = SnippetSerializer(snippet, data=data)

new:
serializer = SnippetSerializer(snippet, data=request.DATA)
'''
