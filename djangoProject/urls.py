"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('playlists.urls',namespace='default')),
    path('admin/', admin.site.urls),
    path('library/', include('songs.urls',namespace='library')),
    path('artists/', include('songs.urls',namespace='artists')),
    path('login/', include('playlists.urls',namespace='login')),
    path('signup/', include('playlists.urls',namespace='signup')),
    path('logout/', include('playlists.urls',namespace='logout')),
    path('songList/', include('songs.urls', namespace='songList')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
