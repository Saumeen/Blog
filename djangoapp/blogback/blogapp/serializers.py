from django.contrib.auth.models import User
from rest_framework import serializers
from blogapp.models import Movie,BlogHome

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'desc')

class BlogHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogHome
        fields =  ('name','aboutme')
