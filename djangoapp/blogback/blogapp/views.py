from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from blogapp.serializers import MovieSerializer,BlogHomeSerializer
from blogapp.models import Movie,BlogHome

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class BlogHomeViewSet(viewsets.ModelViewSet):
    queryset = BlogHome.objects.all()
    serializer_class = BlogHomeSerializer
