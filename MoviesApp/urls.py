from django.urls import path

from . import views
from . import creates_view

urlpatterns = [
    path('/create_movie', creates_view.CreateMovie.as_view(), name='create_movie'),
    path('/create_director' , creates_view.CreateDirector.as_view() , name = 'create_director'),
    path('/create_actor' , creates_view.CreateActor.as_view() , name = 'create_actor'),
    path('/list_movie', views.MovieProcess.as_view(), name='list_movie'),
    path('/list_movie/<int:id>',views.MovieProcess.as_view(), name = 'list_movie'),
    #login
    path('/' , views.Login.as_view(), name = 'login'),

]

