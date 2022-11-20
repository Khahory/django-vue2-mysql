from django.urls import path
from .views import AnimeListView, AnimeDetailView


app_name = "anime"

urlpatterns = [
    path('animes/', AnimeListView.as_view(), name='anime-list'),
    path('anime/<anime_slug>/', AnimeDetailView.as_view(), name='anime-detail'),
]