import sys

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Anime
from .serializers import AnimeSerializer

from pprint import pprint


# Create your views here.
class AnimeListView(APIView):
    def get(self, request, *args, **kwargs):
        # get post                  #los promeros 5
        animes = Anime.animeObjects.all()[0:5]
        serializer = AnimeSerializer(animes, many=True)

        return Response(serializer.data)


class AnimeDetailView(APIView):
    def get(self, request, anime_slug, *args, **kwargs):
        anime = get_object_or_404(Anime, slug=anime_slug)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)


class AnimeListViewQuery(APIView):
    def get(self, request, *args, **kwargs):
        # get post                  #los promeros 5
        animes = Anime.objects.raw('SELECT * FROM anime_anime')
        serializer = AnimeSerializer(animes, many=True)

        # mpstrando en consola
        print('------------------------------------------------------')
        for a in Anime.objects.raw('SELECT * FROM anime_anime'):
            pprint(a.hola)
        print('------------------------------------------------------')

        return Response(serializer.data)
