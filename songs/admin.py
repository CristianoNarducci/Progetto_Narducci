from django.contrib import admin

# Register your models here.
from .models import Song, Artist, Album

admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Album)
