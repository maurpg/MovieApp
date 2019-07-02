from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.renderers import JSONRenderer
from MoviesApp.models import *
from MoviesApp.api.serializer import MovieSerializer, MovieSerializerRest
from MoviesApp.forms import *
from django.shortcuts import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .queryset import search
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BaseAuthentication
from rest_framework import authtoken
from .api.permissions import IsAuthenticatedOrReadOnlyCustom, PermitionsAlterMovies
from .api.filters import MovieFilter


class MovieList(ListView):
    """class to render all movie register"""
    model = Movie
    template_name = 'MoviesApp/list_movie.html'

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)
        context['form'] = SearchMovieForm()
        try:
            movies = search(self.request.GET)
            context['movies'] = movies
            context.update({'object_list': movies})
            context['object_list'] = movies

        except:
            pass
        return context


class DetailMovie(DetailView):
    """class to show info of movie selected"""
    context_object_name = 'movie'
    model = Movie
    template_name = 'MoviesApp/rate_movie.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        """save rate of movie in to MovieRate"""
        rate_movie = Movie_Rate()
        form = dict(request.POST)
        del form['csrfmiddlewaretoken']
        movie = Movie.objects.get(id=form.get('id')[0])
        rate = form.get('rate')
        coment = form.get('coment')[0]

        rate_movie.movie = movie
        rate_movie.coment = coment
        rate_movie.cualifity = rate_movie
        rate_movie.user = request.user
        rate_movie.save()
        return HttpResponse('nothing')


class ResponseMovie(ListView):
    template_name = 'MoviesApp/rate_movie.html'
    model = Movie
    queryset = Movie.objects.all()
    context_object_name = 'movie_seriealizer'

    def get_context_data(self, *args, object_list=None, **kwargs):
        data = super(ResponseMovie, self).get_context_data(object_list=object_list, **kwargs)
        data.update({'objects': JSONRenderer().render(MovieSerializer(self.queryset, many=True).data)})
        return data

    def render_to_response(self, context, **kwargs):
        response = context.get('objects', '')
        return HttpResponse(response, content_type=self.content_type)


class DetailMovieSerialize(DetailView):
    model = Movie
    pk_url_kwarg = 'id'
    template_name = 'MoviesApp/rate_movie.html'

    def get_context_data(self, object=None, *args, **kwargs):
        data = super(DetailMovieSerialize, self).get_context_data(object=object, **kwargs)
        data.update({'object': self.get_object()})
        return data

    def render_to_response(self, context, **response_kwargs):
        data = JSONRenderer().render(MovieSerializer(context.get('object', '')).data)
        return HttpResponse(data, content_type=self.content_type)


class MovieListView(ListAPIView):
    queryset = MovieSerial.objects.all()
    serializer_class = MovieSerializerRest


class MovieDetailView(RetrieveAPIView):
    queryset = MovieSerial.objects.all()
    serializer_class = MovieSerializerRest
    lookup_field = 'pk'


class MovieCreateView(CreateAPIView):
    # queryset = Movie.objects.all()
    model = MovieSerial
    serializer_class = MovieSerializerRest

class MovieRest(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = MovieSerial.objects.all()
    serializer_class = MovieSerializerRest
    permission_classes = [PermitionsAlterMovies]
    filterset_class = MovieFilter

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        data_serialize = MovieSerializerRest(self.get_queryset(), many=True)
        return Response(data_serialize.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
