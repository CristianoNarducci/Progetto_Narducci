# Generated by Django 4.2.1 on 2023-05-22 09:56

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_artist_died_album_alter_song_album'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='song',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='nationality',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
