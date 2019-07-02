from django.views import View
from MoviesApp.forms import *
from django.contrib.auth import login as auth_login, authenticate, logout
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from .api.token import generate_token , destroy_token
import uuid

class Login(View):
    def __init__(self):
        """inizitializate the atributes of class"""
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
                auth_login(request, user)
                generate_token(user)
                return redirect('movie_rest')
            else:
                print('no valid')
                return render(request, self.template, {'form': form_login})


class Logout(View):

    def get(self ,request):
        user = request.user
        destroy_token(user)
        logout(request)
        return redirect('login')