from rest_framework.response import Response
from MoviesApp.models import MovieSerial
from .serializer import MovieSerializerRest
from rest_framework import viewsets

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from MoviesApp.api.permissions import IsAuthenticatedOrReadOnlyCustom

class MovieRestViewSet(viewsets.ModelViewSet):
    """classs mixing for all method of api"""
    queryset = MovieSerial.objects.all()
    serializer_class = MovieSerializerRest

