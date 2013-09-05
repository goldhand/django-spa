from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.decorators import api_view

from rest_framework import generics, permissions, viewsets, mixins

from .models import Book
from .serializers import BookSerializer


@api_view(('GET',))
def library(request, format=None):
    return Response({
        'books': reverse('book-list', request=request, format=format)
    })


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def dispatch(self, *args, **kwargs):
        return super(BookList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def backbone_view(request):
    return render(request, 'books/books.html')
