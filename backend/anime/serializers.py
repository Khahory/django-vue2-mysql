from rest_framework import serializers
from .models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        model = Anime
        fields = ('id', 'titulo', 'descripcion', 'image', 'slug', 'concluido', 'estado')