from django.db import models


class PlaylistManager(models.Manager):
    def for_user_order_by_title(self, user):
        return self.filter(created_by=user).order_by('name')

    def get_playlist_details(self,name):
        return self.filter(name__icontains=name)

    def get_song_detail(self,playlist_name):
        return self.filter(name__icontains=playlist_name).values('song__title')
# Create your models here.


class Playlist(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')
    date_modified = models.DateTimeField('date modified')
    songs = models.ManyToManyField('songs.Song', blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
