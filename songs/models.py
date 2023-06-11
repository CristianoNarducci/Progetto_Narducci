from django.db import models


# Create your models here.
class SongManager(models.Manager):
    def get_song_details(self,name):
        return self.filter(title__icontains=name)
    def get_artist_detail(self,song_name):
        return self.filter(title__icontains=song_name).values('artist__name')


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey('Artist',on_delete=models.DO_NOTHING)
    album = models.ForeignKey('Album',on_delete=models.DO_NOTHING)
    release_date = models.DateField()
    genre = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def getSongName(self):
        return self.title

    object = SongManager()


class Artist(models.Model):
    name = models.CharField(max_length=255)
    artName = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255,null=True, blank=True)
    age = models.IntegerField()
    died = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey('Artist',on_delete=models.DO_NOTHING)
    release_date = models.DateField()

    def __str__(self):
        return self.name

