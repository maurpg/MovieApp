

from django.urls import path

from MoviesApp.api.viewsets import MovieRestViewSet

urlpatterns = [
    path('movie/', MovieRestViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-list-actions'),
    path('movie/<int:pk>/', MovieRestViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}),
         name='movie-detail-actions')
]


