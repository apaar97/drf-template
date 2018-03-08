from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Book, Publisher
from .serializers import UserSerializer, BookSerializer, PublisherSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
