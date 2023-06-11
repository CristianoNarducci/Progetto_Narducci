from django.urls import path
from . import views

app_name = 'songs'
urlpatterns = [
    path('library/', views.library, name='library'),
    path('artists/',views.artists, name='artists'),
    path('songlist/',views.songList, name='songlist'),
    path('addSong/',views.addSong, name='addSong'),
]