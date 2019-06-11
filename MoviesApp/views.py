from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from MoviesApp.models import *
from MoviesApp.forms import LoginForm
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import HttpResponse



class Login(View):

    def __init__(self):
        self.template = 'MoviesApp/login.html'
        self.login_form = LoginForm

    def get(self ,request , *args , **kwargs):
        """return template for login user"""
        logi_form = LoginForm
        return render(request , self.template , {'form':logi_form})

    def post(self , request):
        """validate the autenthicate user """
        form_login = LoginForm(request.POST)
        if form_login.is_valid():
            user_name = form_login.cleaned_data['user_name']
            password = form_login.cleaned_data['password']
            user = authenticate(username=user_name, password=password)
            if user is not None:
                return redirect('list_movie')
            else:
                print('no valid')
                return render(request, self.template, {'form': form_login})


class MovieProcess(View):

    def __init__(self):
        """initials atribute for movie"""
        self.model = Movie
        self.template = 'MoviesApp/list_movie.html'

    def get(self , request , id = None):
        """return movielist template"""
        if id is None:
            movies = Movie.objects.all()
            list_movies = {'list_movie':movies}
            return render(request ,self.template, list_movies)
        movie = Movie.objects.get(id = id)
        return render(request , 'MoviesApp/rate_movie.html' , {'movie':movie})



















