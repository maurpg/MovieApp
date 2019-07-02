from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework import permissions
from rest_framework.views import APIView


class IsAuthenticatedOrReadOnlyCustom(BasePermission):

    def has_permission(self, request, view):
        return request.method.lower() == 'get' or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method.lower() == 'get' or request.user.is_authenticated

class PermitionsAlterMovies(BasePermission):
    """Class for permission routes of project"""
    def __init__(self):
        self.alter_method = [ 'put' , 'delete']
        self.info_method = ['get']

    def has_permission(self, request, view):
        return request.method.lower() in self.info_method or request.user.is_authenticated


