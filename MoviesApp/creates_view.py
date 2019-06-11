from django.shortcuts import render
from django.views.generic import ListView , CreateView , UpdateView , DetailView
from MoviesApp.forms import *
from  MoviesApp.models import *
from  django.urls import reverse_lazy



class CreateMovie(CreateView):
    """class generic view to create a movie"""
    form_class = MovieForm
    model = Movie
    template_name = 'MoviesApp/create_movie.html'
    success_url = reverse_lazy('create_movie')


class CreateDirector(CreateView):
    """class generic to create directot"""
    form_class = MovieDirectorForm
    model = Director
    template_name = 'MoviesApp/create_director.html'
    success_url = reverse_lazy('create_director')


class CreateActor(CreateView):
    """class generic to create actor"""
    form_class = MovieActorForm
    model = Actor
    template_name = 'MoviesApp/create_actor.html'
    success_url = reverse_lazy('create_actor')


class CreateRateMovie(CreateView):
    """class generic to create rate of movie"""
    form_class = MovieRateForm
    model = Movie_Rate
    template_name = 'MoviesApp/create_rate.html'
    success_url = reverse_lazy('rate_movie')

# Create your views here.
