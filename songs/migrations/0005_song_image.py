# Generated by Django 4.2.1 on 2023-05-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_song_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
