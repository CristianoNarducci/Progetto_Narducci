from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Song,Artist
from users import models as users

# Create your views here.
@login_required(redirect_field_name='login/')
def library(request):
    songs = Song.object.all()
    user = users.Profile.objects.get(email=request.user.email)
    return render(request, 'library/library.html', context={'songs': songs, 'user': user})

def artists(request):
    artist = Artist.objects.all()
    song=Song.object.all()
    return render(request, 'artist/artists.html', context={'artist': artist, 'song': song})

@login_required(redirect_field_name='login/')
def songList(request):
    song = Song.object.all()
    user = users.Profile.objects.get(email=request.user.email)
    return render(request, 'Adder/songlist.html', context={'song': song, 'user': user})

def addSong(request):
    if request.method == 'POST':

        song_id = request.POST.get('song_id')
        user_id = request.POST.get('user_id')
        if song_id:
            song = Song.object.get(title=song_id)
            user = users.Profile.objects.get(email=user_id)
            if song not in user.songs.all():
                user.songs.add(song)
                user.save()
                return HttpResponse("La canzone è stata aggiunta alla tua libreria")
            else:
                return HttpResponse("La canzone è già presente nella tua libreria")
