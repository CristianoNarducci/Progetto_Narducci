# Generated by Django 4.2.1 on 2023-06-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0009_remove_song_likes_remove_song_playlist'),
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(blank=True, to='songs.song'),
        ),
    ]