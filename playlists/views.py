from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views import View
import songs.views as lib
import users.models
from .models import Playlist
# Create your views here.


class example(View):
    def get(self,request):
        play = Playlist.objects.all()
        return render(request, 'index.html', {'play': play})

class login(LoginView):
    template_name = 'registration/login.html'
    success_url = '/'

    def get_success_url(self):
        return self.success_url

def logout_view(request):
    logout(request)
    return redirect('/')


def signUpView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            profile = form.save(commit= False)
            profile.user = request.user
            profile.save()
            return redirect('/')  # Reindirizza a una pagina di successo o ad una pagina specifica
    else:
        form = RegistrationForm()

    return render(request, 'registration/signup.html', {'form': form})


class RegistrationForm(UserCreationForm):
    class Meta:
        model = users.models.Profile
        fields = ('username', 'email','age','password1', 'password2')


@login_required(redirect_field_name='/login')
def library(request):
    return lib.library(request)

def artists(request):
    return lib.artists(request)