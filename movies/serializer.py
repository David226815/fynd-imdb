from rest_framework import serializers
from .models import Movies


class moviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

