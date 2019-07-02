from django.urls import path

from . import views , login
from . import creates_view


urlpatterns = [
    path('/create_movie', creates_view.CreateMovie.as_view(), name='create_movie'),
    path('/create_director' , creates_view.CreateDirector.as_view() , name = 'create_director'),
    path('/create_actor' , creates_view.CreateActor.as_view() , name = 'create_actor'),
    path('/list_movie', views.MovieList.as_view(), name='list_movie'),
    path('/detail_movie/<int:id>',views.DetailMovie.as_view(), name = 'detail_movie'),
    path('/movie_serialize',views.ResponseMovie.as_view(), name = 'movie_serialize'),
    #rest
    path('/movie_serialize_model',views.MovieListView.as_view(), name = 'movie_serialize_model'),
    path('/movie_serialize_model/<int:pk>/', views.MovieDetailView.as_view(), name='movie_serialize_detail'),
    path('/movie/serialize/create', views.MovieCreateView.as_view(), name='create'),
    #mixin
    path('/movie_rest', views.MovieRest.as_view() , name = 'movie_rest'),
    path('/movie_rest/<int:pk>/', views.MovieRest.as_view()),



    #login
    path('/' , login.Login.as_view(), name = 'login'),
    path('/logout', login.Logout.as_view(), name='logout'),

]
from rest_framework.urlpatterns import format_suffix_patterns
