from django import forms
from .models import Movie , Movie_Rate , Actor , Director

class MovieForm(forms.ModelForm):

    class Meta:
        model =  Movie

        fields = [
            'title',
            'duration',
            'detail',
            'trailer_url',
            'director',
            'genere',
            'languaje',
            'country',
            'image',
         ]

        labels = {
            'title':'Title',
            'duration':'Duration',
            'detail':'Detail',
            'trailer_url':'Url triler',
            'director':'Director',
            'genere':'Genere',
            'languaje':'Languaje',
            'country':'Country',
            'image':'Image',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'}),
            'trailer_url': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-control'}),
            'genere':forms.Select(attrs={'class': 'form-control'}),
            'languaje': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        



        }


class MovieActorForm(forms.ModelForm):

    class Meta:
        model =  Actor

        fields = [
            'name',
            'age'
        ]

        labels = {
            'name':'Name',
            'age':'Age'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'})
        }


class MovieDirectorForm(forms.ModelForm):

    class Meta:
        model = Director

        fields = [
            'name',
            'age'
        ]

        labels = {
            'name':'Name',
            'age':'Age'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'})
        }


class MovieRateForm(forms.ModelForm):

    class Meta:
        model = Movie_Rate

        fields = [
            'movie',
            'coment'
        ]

        labels = {
            'name':'Name',
            'coment':'coment'
        }

        widgets = {
            'movie': forms.Select(attrs={'class': 'form-control'}),
            'coment': forms.Select(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    user_name = forms.CharField(label='user_name' , max_length=100)
    password = forms.CharField(label='password' , widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    user_name = forms.CharField(label = 'user_name' , max_length=100)
    password =  forms.CharField(label='password' , widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput)

